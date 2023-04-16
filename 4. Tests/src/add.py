import sys

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}


# Вывести ФИО по номеру документа
def human_output(document_number):
    for i in documents:
        if i["number"] == document_number:
            return i["name"]
    else:
        return None


# Вывод номера полки по номеру документа
def document_output(document_number):
    for key, value in directories.items():
        if document_number in value:
            return key
    else:
        return None


# Вывод всех документов
def output_all_documents():
    str_docs_info = "\n"
    for current_document in documents:
        doc_type = current_document["type"]
        doc_number = current_document["number"]
        doc_owner_name = current_document["name"]
        str_docs_info_line = doc_type + " " + doc_number + " " + doc_owner_name + "\n"
        str_docs_info += str_docs_info_line
    return str_docs_info


# Создание полки
def creating_new_shelf(target_shelf):
    if target_shelf in directories:
        return False
    else:
        directories[target_shelf] = []
        return True


# Добавление документа на полку
def append_doc_to_shelf(document_number, target_shelf):
    creating_new_shelf(target_shelf)
    directories[target_shelf].append(document_number)


# Добавление документа в перечень и на полку
def add_new_document(document_number, type_document, owner_name, target_shelf):
    new_doc = {"type": type_document, "number": document_number, "name": owner_name}
    documents.append(new_doc)
    append_doc_to_shelf(document_number, target_shelf)
    return target_shelf


# Удаление документа
def delete_document(document_number):
    for key, value in directories.items():
        if document_number in directories[key]:
            directories[key].remove(document_number)
            res_1 = True
            break
    for i in documents:
        if i["number"] == document_number:
            documents.remove(i)
            res_2 = True
            break
    else:
        res_1, res_2 = False, False
    return res_1, res_2, document_number


# Переместить документ
def document_migration(document_number, target_shelf):
    for key, value in directories.items():
        if document_number in directories[key]:
            directories[key].remove(document_number)
            append_doc_to_shelf(document_number, target_shelf)
            return True
        else:
            return False


def secretary_program_start():
    print(
        """Список команд:
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит.
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится.
    l– list – команда, которая выведет список всех документов.
    a – add – команда, которая добавит новый документ в каталог и в перечень полок.
    d – delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер из перечня полок. 
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. 
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.
    x - exit - команда, которая прекрашает работу программы."""
    )
    run = True
    while run:
        command = input("Введите команду: ")
        if command == "people" or command == "p":
            document_number = input("Введите номер документа: ")
            result = human_output(document_number)
            if result:
                print("Владелец документа: {}".format(result))
            elif not result:
                print(
                    "Документ № {} отсутствует в базе, повторите запрос.".format(
                        document_number
                    )
                )
        elif command == "shelf" or command == "s":
            document_number = input("Введите номер документа: ")
            result = document_output(document_number)
            if result:
                print("Документ находится на полке № {}".format(result))
            elif not result:
                print(
                    "Документ № {} отсутствует в базе, повторите запрос.".format(
                        document_number
                    )
                )
        elif command == "list" or command == "l":
            docs_info = output_all_documents()
            print(f"Список всех документов: {docs_info}")
        elif command == "add" or command == "a":
            document_number = input("Введите номер документа: ")
            type_document = input("Введите тип документа: ")
            owner_name = input("Введите владельца: ")
            target_shelf = input("Ведите номер полки: ")
            result = add_new_document(
                document_number, type_document, owner_name, target_shelf
            )
            print('\nНа полку "{}" добавлен новый документ:'.format(result))
            print("Список документов", *documents, sep="\n")
            print("Список полок", directories, sep="\n")
        elif command == "delete" or command == "d":
            document_number = input("Введите номер документа: ")
            res_1, res_2, doc_num = delete_document(document_number)
            if res_1:
                print("Данные удалины из перечня полок:\n{}".format(directories))
            if res_2:
                print("Данные удалены из католога:", *documents, sep="\n")
            if not res_1 and not res_2:
                print(
                    "Документ № {} отсутствует в базе, повторите запрос.".format(
                        doc_num
                    )
                )
        elif command == "move" or command == "m":
            document_number = input("Введите номер документа: ")
            target_shelf = input("Введите номер целевой полки: ")
            result = document_migration(document_number, target_shelf)
            if result:
                print(
                    "Документ номер {} был перемещен на полку номер {}".format(
                        document_number, target_shelf
                    )
                )
                print("Перечнь полок: ", directories, sep="\n")
            else:
                print(
                    f"Некорректно введён номер документа или полки, повторите запрос."
                )
        elif command == "add shelf" or command == "as":
            target_shelf = input("Введите номер целевой полки: ")
            result = creating_new_shelf(target_shelf)
            if result:
                print("Добавлена полка: {}".format(target_shelf))
                print(directories)
            else:
                print("Полка {} уже существует.".format(target_shelf))
        elif command == "x" or command == "exit":
            print(f"Завершение рабочего сеанаса. До свидания!")
            sys.exit()
        else:
            print(f"Некорректно введена команда, повторите запрос.")


if __name__ == "__main__":
    secretary_program_start()
