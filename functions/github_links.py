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
        'asdr.com',
    )


def get_github_project(url: str) -> str | None:
    try:
        _, _, domain, _, *remain = url.split('/')
    except ValueError:
        return None
    if domain != DOMAIN:
        return None
    return remain[0].split('.')[0]


# <=== async/await ===>
async def _get_valid(urls: tuple[str]) -> tuple[str]:
    async with httpx.AsyncClient() as client:
        for url in urls:
            try:
                response = await client.get(url)
                if response.status_code in (200, 301, 302):
                    yield url
            except ValueError:
                pass  


@decorators.atimer
async def _get_github_projects(urls):
    return [project for project in [get_github_project(url)
            async for url in _get_valid(urls)]
            if project is not None]
# </=== async/await ===>


# <=== asyncio.gather() ===> approx. 3-4 times faster 
async def get_url(client, url):
    try:
        response = await client.get(url)
    except (httpx.UnsupportedProtocol, ValueError):
        return None
    return url if response.status_code in (200, 301, 302) else None


async def gather_valid(urls: tuple[str]) -> tuple[str]:
    async with httpx.AsyncClient() as client:
        coros = [get_url(client, url) for url in urls]
        return [url for url in await asyncio.gather(*coros)
                if url is not None]


@decorators.atimer
async def gather_github_projects(urls):
    return [project for project in [get_github_project(url)
            for url in await gather_valid(urls)]
            if project is not None]
# </=== asyncio.gather() ===>


async def run_together():
    res1 = await _get_github_projects(__get_test_data())
    res2 = await gather_github_projects(__get_test_data())
    assert res1 == res2
    return res2


@decorators.timer
@decorators.output(title=__doc__)
def main():
    return asyncio.run(run_together())


if __name__ == '__main__':
    main()
