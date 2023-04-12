import os
import datetime


def building_path(folder_name, file_name):
    current = os.getcwd()
    full_path = os.path.join(current, folder_name, file_name)
    return full_path


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            date = datetime.datetime.now()
            result = old_function(*args, **kwargs)
            writing_to_file = (
                f"Дата вызова: {date.strftime('%d.%m.%Y')}\nВремя вызова: {date.strftime('%H:%M:%S.%f')}\n"
                f"Имя функции: {old_function.__name__}\n"
                f"Аргументы: {args} {kwargs}\n"
                f"Результат: {result}\n\n"
            )
            with open(
                building_path("3. Decorators\Task_3", path), "a", encoding="utf8"
            ) as wrt:
                wrt.write(writing_to_file)
            return result

        return new_function

    return __logger
