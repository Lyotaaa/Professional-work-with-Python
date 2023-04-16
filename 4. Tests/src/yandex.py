import requests
from configparser import ConfigParser
import json
from pprint import pprint
import sys


def open_a_token(file_name):
    cofing = ConfigParser()
    cofing.read(file_name)
    token = cofing["token_info"]["Yandex_token"]
    return token


class YandexDisk:
    def __init__(self, folder_name, token):
        self.token = token
        self.folder_name = folder_name
        self.url_resources = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {"Authorization": self.token}
        self.params = {"path": self.folder_name}

    def get_folder(self):
        response = requests.get(
            url=self.url_resources, headers=self.headers, params=self.params
        )
        if response.status_code == 200:
            # json_text = json.loads(response.text)
            return True, response.status_code
        elif response.status_code != 200:
            return False, self.folder_name

    def create_a_folder(self):
        respons_get_folder = self.get_folder()
        if respons_get_folder[0]:
            return False, self.folder_name
        else:
            response = requests.put(
                url=self.url_resources, headers=self.headers, params=self.params
            )
            return True, response.status_code

    def delete_folder(self):
        respons_get_folder = self.get_folder()
        if respons_get_folder[0]:
            response = requests.delete(
                url=self.url_resources, headers=self.headers, params=self.params
            )
            return True, response.status_code
        else:
            return False, self.folder_name


if __name__ == "__main__":

    def yandex_info():
        folder_name = input("Введите назание папки: ")
        res_YA = YandexDisk(folder_name, open_a_token("confing.ini"))
        return res_YA

    print(
        """Список команд:
    gf – Информация о папке.
    cr – добавить папку.
    df – удалить папку.
    ex - завершение работы."""
    )
    while True:
        command = input("Ведите команду: ")
        if command == "gf":
            res_YA = yandex_info()
            result = res_YA.get_folder()
            if result[0]:
                print("Такая папка уже есть. Статус код: {}".format(result[1]))
            else:
                print("Папки с именем {} нет.".format(result[1]))
        elif command == "cr":
            res_YA = yandex_info()
            result = res_YA.create_a_folder()
            if result[0]:
                print("Папка успешно создана. Статус код: {}".format(result[1]))
            else:
                print("Папка с именем {} уже существует.".format(result[1]))
        elif command == "df":
            res_YA = yandex_info()
            result = res_YA.delete_folder()
            if result[0]:
                print("Папка успешно удалена. Статус код: {}".format(result[1]))
            else:
                print("Папки с именем {} нет.".format(result[1]))
        elif command == "ex":
            sys.exit()
