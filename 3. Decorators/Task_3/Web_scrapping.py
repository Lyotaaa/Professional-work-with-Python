import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
from tqdm import tqdm
import re
import os
import json
from Task_3.Task_3 import logger

@logger("log_0.log")
def get_headers():
    return Headers(browser="chrome", os="win").generate()


@logger("log_1.log")
def main_page_search(url):
    hh_main_html = requests.get(url=url, headers=get_headers()).text
    hh_main_soup = BeautifulSoup(hh_main_html, "lxml")
    tag_all_vacancy = hh_main_soup.find_all("div", class_="serp-item")
    return tag_all_vacancy


@logger("log_2.log")
def job_search(tag_vacancy):
    link_vacancy = tag_vacancy.find("a", class_="serp-item__title")["href"]
    if tag_vacancy.find("span", class_="bloko-header-section-3") == None:
        salary_vacancy = f"Зарлата не указана"
    else:
        salary_vacancy = tag_vacancy.find("span", class_="bloko-header-section-3").text
    name_company_vacancy = tag_vacancy.find(
        "a", "bloko-link bloko-link_kind-tertiary"
    ).text
    city_vacancy = tag_vacancy.find(
        attrs={"data-qa": "vacancy-serp__vacancy-address"}
    ).text
    tag_description = requests.get(url=link_vacancy, headers=get_headers()).text
    tag_description_soup = BeautifulSoup(tag_description, "lxml")
    description_vacancy = tag_description_soup.find("div", class_="g-user-content").text
    return {
        "link": link_vacancy,
        "salary": salary_vacancy,
        "name_company": name_company_vacancy,
        "city": city_vacancy,
        "description": description_vacancy,
    }


@logger("log_3.log")
def query_search(main_page):
    total_list = []
    for tag_vacancy in tqdm(main_page):
        jobs_found = job_search(tag_vacancy)
        jobs_desc = jobs_found["description"]
        pattern = re.findall(
            r"([Dd]jango.*[Ff]lask)|([Ff]lask.*[Dd]jango)|([Ff]lask.*\s*.*[Dd]jango)",
            jobs_desc,
        )
        if pattern != []:
            _ = jobs_found.pop("description", None)
            total_list.append(jobs_found)
    return total_list


def write_file(folder_name, file_name, total_list):
    current = os.getcwd()
    full_path = os.path.join(current, folder_name, file_name)
    with open(full_path, "w", encoding="utf=8") as w:
        json.dump(total_list, w, ensure_ascii=False, indent=2)


@logger("log_4.log")
def startup():
    main_page = main_page_search(
        "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"
    )
    result = query_search(main_page)
    return result
