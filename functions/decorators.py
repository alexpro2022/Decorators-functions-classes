import time

INPUT_MSG = '\nТестовые данные:\n  {}\n'
OUTPUT_MSG = '\nРезультат выполнения функции:\n  {}\n'
TIMER_MSG = '\nВремя выполнения функции "{}" составило {:.5f} секунд.\n'


def pretty_list(item):
    if isinstance(item, dict | str):
        return item
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
        print(*args)
        result = func(*args, **kwargs)
        if result is not None:
            print(OUTPUT_MSG.format(pretty_list(result)))
        return result
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(TIMER_MSG.format(func.__name__, time.time() - start_time))
        return result
    return wrapper


def atimer(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        print(TIMER_MSG.format(func.__name__, time.time() - start_time))
        return result
    return wrapper
