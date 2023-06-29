"""
A. Функция принимает в качестве аргумента набор ссылок. Ссылки имеют
   формат ссылок на проекты на гитхабе (например:
   https://github.com/miguelgrinberg/Flask-SocketIO,
   https://github.com/miguelgrinberg/Flask-SocketIO.git).
   Функция должна обработать полученные ссылки и вывести в консоль названия
   самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".
"""
import asyncio
import os
import sys

import httpx

if __package__:
    from . import decorators
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators


DOMAIN = 'github.com'
TEST_DATA_SIZE = 10
OK_STATUSES = (200, 301, 302)


@decorators.input
def __get_test_data() -> tuple[str]:
    return (
        'https://github.com/alexpro2022/cargo_transportation-FastAPI.git',
        'https://github.com/miguelgrinberg/Flask-SocketIO',
        'https://github.com/miguelgrinberg/Flask-SocketIO.git',
        'https://docs.aiohttp.org/en/stable/',
        'https://fastapi.tiangolo.com/tutorial/',
        'https://github.com/tiangolo/fastapi.git',
        'https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker.git',
        'https://ya.ru',
        # 'asdr.com',
    ) * TEST_DATA_SIZE


def get_github_project(url: str) -> str | None:
    try:
        _, _, domain, _, *remain = url.split('/')
    except ValueError:
        return None
    if domain != DOMAIN:
        return None
    return remain[0].split('.')[0]


# <=== sync ===>
def sync_valid(urls: tuple[str]) -> tuple[str]:
    return [url for url in urls if httpx.get(url).status_code in OK_STATUSES]


@decorators.timer
def sync_github_projects(urls):
    return [project for project in [get_github_project(url)
            for url in sync_valid(urls)]
            if project is not None]
# </=== sync ===>


# <=== async/await ===>
async def async_valid(urls: tuple[str]) -> tuple[str]:
    async with httpx.AsyncClient(http2=True) as client:
        for url in urls:
            try:
                response = await client.get(url)
                if response.status_code in OK_STATUSES:
                    yield url
            except ValueError:
                pass


@decorators.atimer
async def async_github_projects(urls):
    return [project for project in [get_github_project(url)
            async for url in async_valid(urls)]
            if project is not None]
# </=== async/await ===>


async def get_url(client, url):
    try:
        response = await client.get(url)
    except (httpx.UnsupportedProtocol, ValueError):
        return None
    return url if response.status_code in OK_STATUSES else None


# <=== asyncio.gather() ===> approx. 3-4 times faster then above method
async def gather_valid(urls: tuple[str]) -> tuple[str]:
    async with httpx.AsyncClient(http2=True) as client:
        coros = [get_url(client, url) for url in urls]
        return [url for url in await asyncio.gather(*coros)
                if url is not None]


@decorators.atimer
async def gather_github_projects(urls):
    return [project for project in [get_github_project(url)
            for url in await gather_valid(urls)]
            if project is not None]
# </=== asyncio.gather() ===>


# </=== asyncio.as_completed() ===>  usually a bit faster then gather
async def as_completed_valid(urls: tuple[str]):
    async with httpx.AsyncClient(http2=True) as client:
        coros = [get_url(client, url) for url in urls]
        for coro in asyncio.as_completed(coros):
            url = await coro
            if url is not None:
                yield url


@decorators.atimer
async def as_completed_github_projects(urls):
    return [project for project in [get_github_project(url)
            async for url in as_completed_valid(urls)]
            if project is not None]
# </=== asyncio.as_completed() ===>


async def run_together():
    data = __get_test_data()
    res2 = gather_github_projects(data)
    res3 = as_completed_github_projects(data)
    await asyncio.gather(res2, res3)
    res1 = await async_github_projects(data)
    res4 = sync_github_projects(data)
    assert res1 == res4
    return set(res1)


@decorators.timer
@decorators.output(title=__doc__)
def main():
    return asyncio.run(run_together())


if __name__ == '__main__':
    main()


'''
⏳ Время выполнения функции "as_completed_github_projects" составило 810 ms.

⏳ Время выполнения функции "gather_github_projects" составило 868 ms.

⏳ Время выполнения функции "async_github_projects" составило 4506 ms.

⏳ Время выполнения функции "sync_github_projects" составило 12813 ms.

'''
