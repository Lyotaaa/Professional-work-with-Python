import os
import datetime


def building_path(folder_name, file_name):
    current = os.getcwd()
    full_path = os.path.join(current, folder_name, file_name)
    return full_path


def logger(old_function):
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
            building_path("3. Decorators\Task_1", "main.log"), "a", encoding="utf8"
        ) as wrt:
            wrt.write(writing_to_file)
        return result

    return new_function


def test_1():
    path = building_path("3. Decorators\Task_1", "main.log")
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return "Hello World"

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert "Hello World" == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), "Должно вернуться целое число"
    assert result == 4, "2 + 2 = 4"
    result = div(6, 2)
    assert result == 3, "6 / 2 = 3"

    assert os.path.exists(path), "файл main.log должен существовать"

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, encoding="utf8") as log_file:
        log_file_content = log_file.read()

    assert "summator" in log_file_content, "должно записаться имя функции"
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f"{item} должен быть записан в файл"
