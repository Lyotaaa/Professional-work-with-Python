import sys

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}


def human_output(documents):
    document_number = input("Введите номер документа: ")
    for i in documents:
        if i["number"] == document_number:
            return "Владелец документа: {}".format(i["name"])
    else:
        return "Документ № {} отсутствует в базе, повторите запрос.".format(
            document_number
        )


def document_output(directories):
    document_number = input("Введите номер документа: ")
    for key, value in directories.items():
        if document_number in value:
            return "Документ находится на полке № {}".format(key)
    else:
        return "Документ № {} отсутствует в базе, повторите запрос.".format(
            document_number
        )


def output_all_documents(documents):
    for i in documents:
        doc_type = i["type"]
        doc_number = i["number"]
        doc_name = i["name"]
        print(
            "Имя: {:<18} | документ: {:<10} | № документа: {:<10}".format(
                doc_name, doc_type, doc_number
            )
        )


def add_new_document(documents, directories):
    document_number = input("Введите номер документа: ")
    type_document = input("Введите тип документа: ")
    owner_name = input("Введите владельца: ")
    target_shelf = input("Ведите номер полки: ")
    if target_shelf not in directories:
        return "Такой полки не существует, повторите запрос."
    elif target_shelf in directories:
        documents.append(
            {"type": type_document, "number": document_number, "name": owner_name}
        )
        directories[target_shelf].append(document_number)
        print("Документ добавлен в католог:", *documents, sep="\n")
        return "Документ добавлен на полку № {}:\nСписок полок:\n{}".format(
            target_shelf, directories
        )


def delete_document(documents, directories):
    document_number = input("Введите номер документа: ")
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


def document_migration(directories):
    document_number = input("Введите номер документа: ")
    target_shelf = input("Введите номер целевой полки: ")
    for key, value in directories.items():
        if document_number in directories[key] and target_shelf in directories:
            directories[target_shelf].append(document_number)
            directories[key].remove(document_number)
            res = True
            break
    else:
        res = False
    return res


def creating_new_shelf(directories):
    shelf_number = input("Для создания полки введите номер полки: ")
    if shelf_number in directories:
        return False, shelf_number
    else:
        directories[shelf_number] = []
        return True, shelf_number


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

if __name__ == "__main__":
    run = True
    while run:
        command = input("Введите команду: ")
        if command == "people" or command == "p":
            result = human_output(documents)
            print(result)
        elif command == "shelf" or command == "s":
            result = document_output(directories)
            print(result)
        elif command == "list" or command == "l":
            output_all_documents(documents)
        elif command == "add" or command == "a":
            result = add_new_document(documents, directories)
            print(result)
        elif command == "delete" or command == "d":
            res_1, res_2, doc_num = delete_document(documents, directories)
            if res_1:
                print("Данные удалины из перечня полок: {}".format(directories))
            if res_2:
                print("Данные удалены из католога:", *documents, sep="\n")
            if not res_1 and not res_2:
                print(
                    "Документ № {} отсутствует в базе, повторите запрос.".format(
                        doc_num
                    )
                )
        elif command == "move" or command == "m":
            if document_migration(directories):
                print("Документ перемещен: {}".format(directories))
            else:
                print(
                    f"Некорректно введён номер документа или полка, повторите запрос."
                )
        elif command == "add shelf" or command == "as":
            res, shelf_num = creating_new_shelf(directories)
            if res:
                print("Добавлена полка: {}".format(shelf_num))
                print(directories)
            else:
                print("Полка {} уже существует, повторите запрос.".format(shelf_num))
        elif command == "x" or command == "exit":
            print(f"Завершение рабочего сеанаса. До свидания!")
            sys.exit()
        else:
            print(f"Некорректно введена команда, повторите запрос.")
