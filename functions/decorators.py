import logging
import time
from typing import Any

INPUT_MSG = '\nТестовые данные:\n  {}\n'
OUTPUT_MSG = '\nРезультат выполнения функции:\n  {}\n'
TIMER_MSG = ' Время выполнения функции "{}" составило {:.0f} миллисек.\n'
TEXT_MAX_SIZE = 2000

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def pretty_list(item):
    if isinstance(item, dict):
        return item
    if isinstance(item, str):
        return item[:TEXT_MAX_SIZE] + ' ...'
    try:
        return '\n  '.join(item)
    except TypeError:
        return item


def input(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(INPUT_MSG.format(pretty_list(result)))
        return result
    return wrapper


def output(func):
    def wrapper(*args, **kwargs):
        print('\n' + '='*50)
        result = func(*args, **kwargs)
        if result is not None:
            print(OUTPUT_MSG.format(pretty_list(result)))
        return result
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        logging.info(TIMER_MSG.format(
            func.__name__, (time.time() - start_time)*1000))
        return result
    return wrapper


def atimer(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        logging.info(TIMER_MSG.format(
            func.__name__, (time.time() - start_time)*1000))
        return result
    return wrapper


def timer_all_public_methods(cls):
    class Timer:
        def __init__(self, *args, **kwargs):
            self.obj = cls(*args, **kwargs)

        def __getattribute__(self, __name: str) -> Any:
            try:
                return super().__getattribute__(__name)
            except AttributeError:
                attr = self.obj.__getattribute__(__name)
                if (
                    not isinstance(attr, type(self.__init__))
                    or __name.startswith('_')
                ):
                    return attr
                return timer(attr)

    return Timer
