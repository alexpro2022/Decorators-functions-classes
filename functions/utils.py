import random
from string import ascii_letters


def get_random_str(str_length):
    return ''.join([random.choice(ascii_letters)
                    for _ in range(str_length)])
