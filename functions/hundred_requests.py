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

TEST_URL: str = 'http://httpbin.org/delay/3'
TASKS_AMOUNT: int = 100
MAX_TIMEOUT: float = 9.99


@decorators.input
def __get_test_data():
    return TEST_URL


async def get_url(session, url):
    try:
        async with session.get(url) as response:
            return response
    except aiohttp.ServerDisconnectedError:
        pass


@decorators.atimer
async def test_url(url):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(get_url(session, url))
                 for _ in range(TASKS_AMOUNT)]
        done, pending = await asyncio.wait(tasks, timeout=MAX_TIMEOUT)
        return f'done = {len(done)}', f'pending = {len(pending)}'


@decorators.timer
@decorators.output(title=__doc__)
def main():
    return asyncio.run(test_url(__get_test_data()))


if __name__ == '__main__':
    main()
