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
            print(i["name"])
            break
    else:
        print(f"Документ № {document_number} отсутствует в базе, повторите запрос.")
        human_output(documents)


def document_output(directories):
    document_number = input("Введите номер документа: ")
    for key, value in directories.items():
        if document_number in value:
            print(f"Документ находится на полке № {key}")
            break
    else:
        print(f"Документ № {document_number} отсутствует в базе, повторите запрос.")
        # document_output(directories)


def output_all_documents(documents):
    for i in documents:
        print(i["type"], i["number"], i["name"])


def add_new_document(documents, directories):
    document_number = input("Введите номер документа: ")
    type_document = input("Введите тип документа: ")
    owner_name = input("Введите владельца: ")
    target_shelf = input("Ведите номер полки: ")
    if target_shelf not in directories:
        print(f"Такой полки не существует, повторите запрос.")
        # add_new_document(documents, directories)
    elif target_shelf in directories:
        documents.append(
            {"type": type_document, "number": document_number, "name": owner_name}
        )
        directories[target_shelf].append(document_number)
        print(f"Документ добавлен на полку № {target_shelf}: {directories}")
        print(f"Документ добавлен в католог:", *documents, sep="\n")


def delete_document(documents, directories):
    document_number = input("Введите номер документа: ")
    for key, value in directories.items():
        if document_number in directories[key]:
            directories[key].remove(document_number)
            print(f"Данные удалины из перечня полок: {directories}")
            break
    for i in documents:
        if i["number"] == document_number:
            documents.remove(i)
            print(f"Данные удалены из католога:", *documents, sep="\n")
            break

    else:
        print(f"Документ № {document_number} отсутствует в базе, повторите запрос.")
        # delete_document(documents, directories)


def document_migration(directories):
    document_number = input("Введите номер документа: ")
    target_shelf = input("Введите номер целевой полки: ")
    for key, value in directories.items():
        if document_number in directories[key] and target_shelf in directories:
            directories[target_shelf].append(document_number)
            directories[key].remove(document_number)
            print(f"Документ перемещен на полку № {target_shelf} {directories}")
            break
    else:
        print(f"Некорректно введён номер документа или полка, повторите запрос.")
        # document_migration(directories)


def creating_new_shelf(directories):
    shelf_number = input("Для создания полки введите номер полки: ")
    if shelf_number in directories:
        print(f"Такая полка уже существует, повторите запрос.")
        # creating_new_shelf(directories)
    else:
        directories[shelf_number] = []
        print(f"Полка создана: {directories}")


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
            human_output(documents)
            # break
        elif command == "shelf" or command == "s":
            document_output(directories)
            # break
        elif command == "list" or command == "l":
            output_all_documents(documents)
            # break
        elif command == "add" or command == "a":
            add_new_document(documents, directories)
            # break
        elif command == "delete" or command == "d":
            delete_document(documents, directories)
            # break
        elif command == "move" or command == "m":
            document_migration(directories)
            # break
        elif command == "add shelf" or command == "as":
            creating_new_shelf(directories)
            # break
        elif command == "x" or command == "exit":
            print(f"Завершение рабочего сеанаса. До свидания!")
            break
        else:
            print(f"Некорректно введена команда, повторите запрос.")
