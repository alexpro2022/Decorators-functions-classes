"""
B. Реализовать функцию, принимающую два списка и возвращающую словарь
   (ключ из первого списка, значение из второго), упорядоченный по ключам.
   Длина первого списка не должна быть равна длине второго.
   Результат вывести в консоль.
"""
import os
import sys
from itertools import zip_longest

if __package__:
    from . import decorators
    from .utils import get_random_str
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators
    from utils import get_random_str


@decorators.input
def __get_test_data(start=0, end=20):
    keys, values = set(), []
    for i in range(start, end):
        keys.add(str(i))
        values.append(i)
    for _ in range(2):        
        keys.pop()
    return list(keys), values


@decorators.timer
def create_dict(keys: list, values: list):
    while len(keys) < len(values):
        keys.append(get_random_str(5))
    return dict(sorted(zip_longest(keys, values, fillvalue='fillvalue')))


@decorators.timer
@decorators.output(title=__doc__)
def main():
    return create_dict(*__get_test_data())


if __name__ == '__main__':
    main()
