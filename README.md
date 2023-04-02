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

---
Сдайте домашнее задание ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).

Мы не сможем проверить задание, если вы пришлёте:

* архивы,
* скриншоты кода,
* теоретический рассказ о возникших проблемах.    

<=============================================================================>

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

---
Домашнее задание сдавайте ссылкой на репозиторий [BitBucket](https://bitbucket.org/) или [GitHub](https://github.com/).

Мы не сможем проверить, если вы пришлёте:

* архивы,
* скриншоты кода,
* теоретический рассказ о возникших проблемах.    



