from pprint import pprint
import os
import csv
from re import sub
import re

current = os.getcwd()
folder_name = '2. Regular expressions'
file_name_r = 'phonebook_raw.csv'
full_path_r = os.path.join(current, folder_name, file_name_r)
# Читаем адресную книгу в формате CSV в список contacts_list
with open(full_path_r, encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
        r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
        r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
new_phone = r'+7(\4)\8-\11-\14\15\17\18\19\20'

res_list = []
for i in contacts_list:
    # print(i)
    res = (",".join(i))
    res = re.sub(pattern, new_phone, res)
    res = res.split(',')
    res_list.append(res)
# print(res_list)
total ={}
r = res_list[2:]
# pprint(r)
result = {}
for name, l_name, s_name, *rest in r:
    info = name + ' ' +l_name + ' ' + s_name
    print(info)
    # result.setdefault(tuple(name, l_name, s_name), []).append(rest) 
# print(result)
# for i in range(len(r)):
    # print(i[0])
    


    # if len(r[i][0].split()) == 3:
        # print(r[i][0])
    #     total[i + 1] = {
    #         'lastname': (r[i][0].split())[0],
    #         'firstname': (r[i][0].split())[1],
    #         'surname': (r[i][0].split())[2],
    #         'organization': r[i][3],
    #         'position': r[i][4],
    #         'phone': r[i][5],
    #         'email':r[i][6]
    #     }
    # elif len(r[i][0].split()) == 2 and r[i][0][1] == None:
    #     total[i + 1] = {
    #         'lastname': (r[i][0].split())[0],
    #         'firstname': (r[i][0].split())[1],
    #         'surname': r[i][2],
    #         'organization': r[i][3],
    #         'position': r[i][4],
    #         'phone': r[i][5],
    #         'email':r[i][6]
    #     }
    # elif len(r[i][0].split()) == 1 and r[i][]:
    #     total[i + 1] = {
    #         'lastname': (r[i][0].split())[0],
    #         'firstname': r[i][1],
    #         'surname': r[i][2],
    #         'organization': r[i][3],
    #         'position': r[i][4],
    #         'phone': r[i][5],
    #         'email':r[i][6]
    #     }
# pprint(total)
'''print(res_list)
total = {}
for i in res_list[1:]:
    # print(i[0])
    if len(i[0].split()) == 3:
        total[i[0]] = []
    if len(i[0].split()) == 2:
        total[i[0] + i[1]] = []'''

# pprint(total)        


# for i in range(len(res_list)):
#     for i in range(len(res_list[i])):





# def change_phone(contacts_list):
#     pattern = r"(8|\+7)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*[\(доб.\s]*(\d{4})*\)*"
#     repl_extra = r"+7(\2)\3-\4-\5 доб.\6"
#     repl = r"+7(\2)\3-\4-\5"
#     for i in contacts_list:
#         if "доб" not in i:
#             i = re.sub(pattern, repl, i)
#         elif "доб" in i:
#             i[5] = re.sub(pattern, repl_extra, i)
#         print(i)
# change_phone(contacts_list)

# pprint(contacts_list)
# 1.  Выполните пункты 1-3 задания.

# information_list = []
    # word_list = re.findall(r"\w+", contacts_list)
    # print(contacts_list)

# 2. Сохраните получившиеся данные в другой файл.
# file_name_w = 'phonebook.csv'
# full_path_w = os.path.join(current, folder_name, file_name_w)
# Код для записи файла в формате CSV:
# with open(full_path_w, "w", encoding="utf8") as f:
#     datawriter = csv.writer(f, delimiter=',')
# # Вместо contacts_list подставьте свой список:
#     datawriter.writerows(contacts_list)

# num_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
#                   r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
#                   r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    
# num_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
# contacts_list_new = list()
# for page in contacts_list:
#   page_string = ','.join(page) # объединение в строку
#   format_page = sub(num_pattern, num_pattern_new, page_string) # замена шаблонов в строке
#   page_list = format_page.split(',') # формируем список строк
#   contacts_list_new.append(page_list)
# print(contacts_list_new[2:4])


pattern = r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*'
# pattern = r"(8|\+7)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*[\(доб.\s]*(\d{4})*\)*"
# 
repl_extra = r"+7(\2)\3-\4-\5 доб.\6 "
repl = r"+7(\2)\3-\4-\5 "
# for i in res_list[2:]:
#     if "доб." not in res_list[2:]:
#         res_list = re.sub(pattern, repl, res_list)
#     elif "доб." in res_list:
#         res_list = re.sub(pattern, repl_extra, res_list)