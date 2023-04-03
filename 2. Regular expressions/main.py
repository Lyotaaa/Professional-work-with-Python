from pprint import pprint
import os
import csv

current = os.getcwd()
folder_name = '2. Regular expressions'
file_name_r = 'phonebook_raw.csv'
full_path_r = os.path.join(current, folder_name, file_name_r)
# Читаем адресную книгу в формате CSV в список contacts_list
with open(full_path_r, encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)
# 1.  Выполните пункты 1-3 задания.
# Ваш код.

# 2. Сохраните получившиеся данные в другой файл.
file_name_w = 'phonebook.csv'
full_path_w = os.path.join(current, folder_name, file_name_w)
# Код для записи файла в формате CSV:
with open(full_path_w, "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список:
    datawriter.writerows(contacts_list)