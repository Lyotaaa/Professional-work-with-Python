from pprint import pprint


def list_filtering():
    geo_logs = [
        {"visit1": ["Москва", "Россия"]},
        {"visit2": ["Дели", "Индия"]},
        {"visit3": ["Владимир", "Россия"]},
        {"visit4": ["Лиссабон", "Португалия"]},
        {"visit5": ["Париж", "Франция"]},
        {"visit6": ["Лиссабон", "Португалия"]},
        {"visit7": ["Тула", "Россия"]},
        {"visit8": ["Тула", "Россия"]},
        {"visit9": ["Курск", "Россия"]},
        {"visit10": ["Архангельск", "Россия"]},
    ]
    result = []
    for visit_list in geo_logs:
        for value in visit_list.values():
            if "Россия" in value:
                result.append(visit_list)
    return result


def get_unique_id():
    ids = {
        "user1": [213, 213, 213, 15, 213],
        "user2": [54, 54, 119, 119, 119],
        "user3": [213, 98, 98, 35],
    }
    total_list = []
    for value in ids.values():
        total_list.extend(value)
    return sorted(list(set(total_list)))


def get_distribution():
    queries = [
        "смотреть сериалы онлайн",
        "новости спорта",
        "афиша кино",
        "курс доллара",
        "сериалы этим летом",
        "курс по питону",
        "сериалы про спорт",
    ]
    total_request_quantity = len(queries)
    temporary_dictionary = {}
    result = []
    for query in queries:
        count = len(query.split())
        temporary_dictionary[count] = temporary_dictionary.get(count, 0) + 1
    for key in temporary_dictionary:
        percent_of_queries = round(
            temporary_dictionary[key] / total_request_quantity * 100, 1
        )
        res = str(key), str(percent_of_queries)
        result.append(res)
    return sorted(result)


def get_sales():
    stats = {
        "email": 42,
        "facebook": 55,
        "ok": 98,
        "google": 99,
        "vk": 115,
        "yandex": 120,
    }

    volume_of_sales = []

    for company, sales in stats.items():
        volume_of_sales.append(sales)
    max_volume_of_sales = max(list(set(volume_of_sales)))
    for company, sales in stats.items():
        if stats[company] == max_volume_of_sales:
            return company


def sort_dict():
    initial_list = ["2018-01-01", "yandex", "cpc", 100, 400, "kek", 2022, "Hello World"]
    received_dictionary = {initial_list[-2]: initial_list[-1]}
    for key in initial_list[:-2][::-1]:
        received_dictionary = {key: received_dictionary}
    return received_dictionary
