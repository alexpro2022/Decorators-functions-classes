"""
C. Реализовать функцию с помощью методов map и lambda. Функция принимает
   список элементов (состоящий из строк и цифр), возвращает новый список,
   с условием - если элемент списка был строкой, в начало строки нужно
   добавить текст "abc_", в конец строки - "_cba". Если элемент был int -
   то его значение нужно возвести в квадрат. Результат вывести в консоль.
"""


import random
from string import ascii_letters


def new_list(arr):
    return list(map(lambda x: x*x if isinstance(x, int)
                    else ''.join(('abc_', x, '_cba')), arr))


if __name__ == '__main__':

    MAX_SIZE = 10
    STRING_LENGTH = 4

    def _get_test_data():
        res = []
        for _ in range(MAX_SIZE):
            res.append(''.join([random.choice(ascii_letters)
                                for _ in range(STRING_LENGTH)]))
            res.append(random.randint(1, 100))
        return res

    print(new_list(_get_test_data()))
