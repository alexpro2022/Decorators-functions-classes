"""
D. Реализовать функцию, которая замеряет время на исполнение 100 запросов к
   адресу: http://httpbin.org/delay/3. Запросы должны выполняться асинхронно.
   Допускается написание вспомогательных функций и использование сторонних
   библиотек. Результат замера времени выводит в консоль.
   Ожидаемое время не должно превышать 10 секунд.
"""
import aiohttp
import asyncio

import os
import sys

if __package__:
    from . import decorators
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators

TEST_URL = 'http://httpbin.org/delay/3'
MAX_SIZE = 100


@decorators.input
def __get_test_data():
    return TEST_URL


async def get_url(session, url):
    async with session.get(url) as response:
        return response


@decorators.atimer
async def test_url(url):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_url(session, url))
                 for _ in range(MAX_SIZE)]
        return await asyncio.gather(*tasks)


@decorators.output
def main(title):
    asyncio.run(test_url(__get_test_data()))


if __name__ == '__main__':
    main(__doc__)
