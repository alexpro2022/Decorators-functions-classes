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

import aiohttp
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


async def get_valid(urls: tuple[str]) -> tuple[str]:
    async with httpx.AsyncClient() as client:
        for url in urls:
            try:
                response = await client.get(url)
            except ValueError:
                continue
            if response.status_code in (200, 301):
                yield url


async def get_github_project(url: str) -> str | None:
    try:
        _, _, domain, _, *remain = url.split('/')
    except ValueError:
        return None
    if domain != DOMAIN:
        return None
    return remain[0].split('.')[0]


@decorators.atimer
async def get_github_projects(urls):
    return [project for project in [await get_github_project(url) async for url in get_valid(urls)]
            if project is not None]


@decorators.timer
@decorators.output(title=__doc__)
def main():
    return asyncio.run(get_github_projects(__get_test_data()))

if __name__ == '__main__':
    main()
