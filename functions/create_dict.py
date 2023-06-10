"""
B. Реализовать функцию, принимающую два списка и возвращающую словарь
   (ключ из первого списка, значение из второго), упорядоченный по ключам.
   Длина первого списка не должна быть равна длине второго.
   Результат вывести в консоль.
"""
import os
import sys

if __package__:
    from . import decorators
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators


@decorators.input
def __get_test_data(start=0, end=20):
    keys, values = set(), []
    for i in range(start, end):
        keys.add(str(i))
        values.append(i)
    keys.pop()
    return list(keys), values


@decorators.timer
def create_dict(keys, values):
    return dict(sorted(zip(keys, values)))


@decorators.output
def main(title):
    return create_dict(*__get_test_data())


if __name__ == '__main__':
    main(__doc__)
