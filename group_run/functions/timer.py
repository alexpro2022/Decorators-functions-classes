"""
D. Реализовать функцию, которая замеряет время на исполнение 100 запросов к
   адресу: http://httpbin.org/delay/3. Запросы должны выполняться асинхронно.
   Допускается написание вспомогательных функций и использование сторонних
   библиотек. Результат замера времени выводит в консоль.
   Ожидаемое время не должно превышать 10 секунд.
"""


import aiohttp
import asyncio
import time

TEST_URL = 'http://httpbin.org/delay/3'
MAX_SIZE = 100


def timer(func):
    MSG = '\nВремя выполнения функции "{}" составило {:.5f} секунд.'

    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        print(MSG.format(func.__name__, time.time() - start_time))
        return result
    return wrapper


async def get_url(session, url):
    async with session.get(url) as response:
        return response


@timer
async def test_url(url):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_url(session, url))
                 for _ in range(MAX_SIZE)]
        return await asyncio.gather(*tasks)


if __name__ == '__main__':
    MSG = '{qty} асинхронных запросов к: {url}'
    # start = time.time()
    results = asyncio.run(test_url(TEST_URL))
    print(MSG.format(qty=MAX_SIZE, url=results[-1].url))
    # print(f'total time = {time.time() - start}')
