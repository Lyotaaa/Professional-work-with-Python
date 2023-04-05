from pprint import pprint
import os
import csv
from re import sub
import re

def find_file(folder_name, file_name):
    current = os.getcwd()
    full_path = os.path.join(current, folder_name, file_name)
    return full_path

def open_file(full_path):
    with open(full_path, encoding="utf8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def pattern():
    pattern = r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)" \
        r"(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
    new_phone = r'+7(\4)\8-\11-\14\15\17\18\20'
    return [pattern, new_phone]

def change_phone(contacts_list):
    res_list = []
    for i in contacts_list:
        res = (",".join(i))
        res = re.sub(pattern()[0], pattern()[1], res)
        res = res.split(',')
        res_list.append(res)
    return res_list 

def view_normalization(res_list):
    normal_view = [' '.join(i[0:3]).split(' ')[0:3] + i[3:7] for i in res_list]
    return normal_view[1:]

def save_contacts_list(normal_view):
    finish_list = []
    for more in normal_view:
        for basic in normal_view:
            if more[0:2] == basic[0:2]:
                basic_list = more
                more = basic_list[0:2]
                for i in range(2, 7):
                    if basic_list[i] == '':
                        more.append(basic[i])
                    else:
                        more.append(basic_list[i])
        if more not in finish_list:
            finish_list.append(more)
    return finish_list

def write_file(folder_name, file_name, finish_list):
    current = os.getcwd()
    full_path = os.path.join(current, folder_name, file_name)
    with open(full_path, "w", encoding="utf8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(finish_list)

if __name__ == '__main__':
    file = find_file('5. Regular expressions', 'phonebook_raw.csv')
    contacts_list = open_file(file)
    normal_phone = change_phone(contacts_list)
    normal_view = view_normalization(normal_phone)
    finish_list = save_contacts_list(normal_view)
    # print(*finish_list,sep="\n")
    write_file('5. Regular expressions', 'phonebook.csv', finish_list)