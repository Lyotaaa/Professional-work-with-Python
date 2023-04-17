# Домашнее задание к лекции 1. «Import. Module. Package»

1. Разработать **структуру** программы «Бухгалтерия»:
- main.py;  
- application/salary.py;  
- application/db/people.py.

Main.py — основной модуль для запуска программы.  
В модуле salary.py функция calculate_salary.  
В модуле people.py функция get_employees.  

2. Импортировать функции в модуль main.py и вызывать эти функции в конструкции.
```
if __name__ == '__main__':
```
**Сами функции реализовывать не нужно**. Достаточно добавить туда какой-либо вывод.

3. Познакомиться с модулем [datetime](https://pythonworld.ru/moduli/modul-datetime.html). 
При вызове функций модуля main.py выводить текущую дату.

4. Найти интересный для себя пакет на [pypi](https://pypi.org/) и в файле requirements.txt указать его с актуальной версией. При желании можно написать программу с этим пакетом.

\*5. Создать рядом с файлом main.py модуль dirty_main.py и импортировать все функции с помощью
конструкции (необязательное задание).
```
from package.module import *
```

<=========================================================================>

# Домашнее задание к лекции 2. «Iterators. Generators. Yield»

1. Доработать класс `FlatIterator` в коде ниже. Должен получиться итератор, который принимает список списков и возвращает их плоское представление, т. е. последовательность, состоящую из вложенных элементов. Функция `test` в коде ниже также должна отработать без ошибок.

```python
class FlatIterator:

    def __init__(self, list_of_list):
        ...

    def __iter__(self):
        ...
        return self

    def __next__(self):
        ...
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
```


2. Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает их плоское представление.
Функция `test` в коде ниже также должна отработать без ошибок.
```python
import types


def flat_generator(list_of_lists):

    ...
    yield
    ...


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    
```

3.__*__ Необязательное задание. Написать итератор, аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности.
Шаблон и тест в коде ниже:
```python
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        ...
        return self
    
    def __next__(self):
        ...
        return item


def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
```

4.__*__ Необязательное задание. Написать генератор, аналогичный генератору из задания 2, но обрабатывающий списки с любым уровнем вложенности.
Шаблон и тест в коде ниже:
```python
import types


def flat_generator(list_of_list):
    ...
    yield
    ...

def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
```

<=========================================================================>

# Домашнее задание к лекции 3. «Decorators»

1. Доработать декоратор `logger` в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log'  дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Функция `test_1` в коде ниже также должна отработать без ошибок.

```python
import os


def logger(old_function):
    ...

    def new_function(*args, **kwargs):
        ...

    return new_function


def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()

```


2. Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Путь к файлу должен передаваться в аргументах декоратора. Функция `test_2` в коде ниже также должна отработать без ошибок.

```python
import os


def logger(path):
    ...
    
    def __logger(old_function):
        def new_function(*args, **kwargs):
            ...

        return new_function

    return __logger


def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()

```

3. Применить написанный логгер к приложению из любого предыдущего д/з.

<=========================================================================>


# Домашнее задание к лекции 4. «Tests»

### Задача 1. Unit-tests
Из курса «Python: программирование на каждый день и сверхбыстрое прототипирование» нужно протестировать программу по работе с бухгалтерией из [лекции 2.1](https://github.com/netology-code/py-homework-basic/tree/master/2.1.functions).
Если у вас есть своё решение этой задачи, можно использовать его или использовать предложенный код в директории src этого задания.

* Следует протестировать основные функции по получению информации о документах, добавлении и удалении элементов из словаря.
  
Рекомендации по тестам:

1. Если у вас в функциях информация выводилась (print), то теперь её лучше возвращать (return), чтобы можно было протестировать.
2. Input можно «замокать» с помощью ```unittest.mock.patch```. Если с этим будут проблемы, то лучше переписать функции так, чтобы данные приходили через параметры.

### Задача 2. Автотест API Яндекса
Проверим правильность работы Яндекс Диск REST API. Напишите тесты, проверяющие создание папки на Диске.  
Используя библиотеку requests, напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой.

Пример положительных тестов:

* код ответа соответствует 200;
* результат создания папки — папка появилась в списке файлов.

### Задача 3. Не обязательная
Применив selenium, напишите unit-test для авторизации на Яндексе по url: https://passport.yandex.ru/auth/.

<=========================================================================>

# Домашнее задание к лекции 5. «Regular expressions»

Иногда при знакомстве мы записываем контакты в адресную книгу кое-как, с мыслью, что когда-нибудь потом всё обязательно поправим. Копируем данные из интернета или из смс. Добавляем людей в разных мессенджерах. В результате получается адресная книга, в которой невозможно кого-то найти: мешает множество дублей и разная запись одних и тех же имен.

Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/.

Ваша задача: починить адресную книгу, используя регулярные выражения.  
Структура данных будет всегда:   
`lastname,firstname,surname,organization,position,phone,email`  
Предполагается, что телефон и e-mail у человека может быть только один.  

Необходимо:

1. Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
2. Привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
3. Объединить все дублирующиеся записи о человеке в одну.  

```python
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
  datawriter.writerows(contacts_list)
```

<=========================================================================>

# Домашнее задание к лекции 6.«Web-scrapping»

Попробуем получать интересующие вакансии на сайте [headhunter](https://spb.hh.ru/) самыми первыми :)

1. Необходимо парсить страницу со свежими вакансиями с поиском по "Python" и городами "Москва" и "Санкт-Петербург". Эти параметры задаются по [ссылке](https://spb.hh.ru/search/vacancy?text=python&area=1&area=2)
2. Нужно выбрать те вакансии, у которых в описании есть ключевые слова "Django" и "Flask".
3. Записать в json информацию о каждой вакансии - ссылка, вилка зп, название компании, город.
---
## Дополнительное (необязательное) задание

Получать вакансии только с ЗП в долларах(USD)

<=========================================================================>

# Домашнее задание к лекции 7. «Подготовка к собеседованию»

**Стек** — абстрактный тип данных, представляющий список элементов, организованных по принципу *LIFO (англ. last in — first out, «последним пришёл — первым вышел»)*. Чаще всего принцип работы стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, нужно снять верхнюю. Или с магазином в огнестрельном оружии: стрельба начнётся с патрона, заряженного последним.

1. Нужно реализовать класс Stack со следующими методами:

- is_empty — проверка стека на пустоту. Метод возвращает True или False;
- push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
- pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
- peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
- size — возвращает количество элементов в стеке.

2. Используя стек из задания 1, решите задачу на проверку сбалансированности скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.

Пример сбалансированных последовательностей скобок:

- ```(((([{}]))))```
- ```[([])((([[[]]])))]{()}```
- ```{{[()]}}```

Несбалансированные последовательности:

- ```}{}```
- ```{{[(])]}}```
- ```[[{())}]```

Программа ожидает на вход строку со скобками. На выход сообщение: «Сбалансированно», если строка корректная, и «Несбалансированно», если строка составлена неверно.

\*3. [Рефакторинг кода (необязательное задание)](PEP8.md).

Задачи, которые помогут подговиться к собеседованиям, можно найти на ресурсах:

- [leetcode](https://leetcode.com/),
- [checkio](https://checkio.org/).

---

Домашнее задание сдавайте ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).

Мы не сможем проверить, если вы пришлёте:

- архивы,
- скриншоты кода,
- теоретический рассказ о возникших проблемах.    

