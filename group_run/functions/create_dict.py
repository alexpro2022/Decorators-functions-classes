"""
B. Реализовать функцию, принимающую два списка и возвращающую словарь
   (ключ из первого списка, значение из второго), упорядоченный по ключам.
   Длина первого списка не должна быть равна длине второго.
   Результат вывести в консоль.
"""


def create_dict(keys, values):
    return dict(sorted(zip(keys, values)))


if __name__ == '__main__':

    def _get_test_data(start=0, end=20):
        keys, values = set(), []
        for i in range(start, end):
            keys.add(str(i))
            values.append(i)
        keys.pop()
        return keys, values

    print(create_dict(*_get_test_data()))
