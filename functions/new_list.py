"""
C. Реализовать функцию с помощью методов map и lambda. Функция принимает
   список элементов (состоящий из строк и цифр), возвращает новый список,
   с условием - если элемент списка был строкой, в начало строки нужно
   добавить текст "abc_", в конец строки - "_cba". Если элемент был int -
   то его значение нужно возвести в квадрат. Результат вывести в консоль.
"""
import random
import os
import sys

if __package__:
    from . import decorators
    from .utils import get_random_str
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators
    from utils import get_random_str


MAX_SIZE = 10
STRING_LENGTH = 4


@decorators.input
def __get_test_data():
    res = []
    for _ in range(MAX_SIZE):
        res.append(get_random_str(STRING_LENGTH))
        res.append(random.randint(1, 100))
    return res


def l_func(item):
    return {
        int: lambda x: x*x,
        str: lambda x: ''.join(('abc_', x, '_cba')),
    }.get(type(item))(item)


@decorators.timer
def new_list(arr):
    res1 = list(map(lambda x: x*x if isinstance(x, int)
                    else ''.join(('abc_', x, '_cba')), arr))
    res2 = list(map(l_func, arr))
    return res1 == res2, res2


@decorators.output
def main(title):
    return new_list(__get_test_data())


if __name__ == '__main__':
    main(__doc__)
