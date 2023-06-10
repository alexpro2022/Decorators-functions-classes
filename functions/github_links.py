"""
A. Функция принимает в качестве аргумента набор ссылок. Ссылки имеют
   формат ссылок на проекты на гитхабе (например:
   https://github.com/miguelgrinberg/Flask-SocketIO,
   https://github.com/miguelgrinberg/Flask-SocketIO.git).
   Функция должна обработать полученные ссылки и вывести в консоль названия
   самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".
"""
import httpx

import os
import sys

if __package__:
    from . import decorators
else:
    sys.path.append(os.path.dirname(__file__) + '/.')
    import decorators


DOMAIN = 'github.com'


@decorators.input
def __get_test_data():
    return (
        'https://github.com/alexpro2022/cargo_transportation-FastAPI.git',
        'https://github.com/miguelgrinberg/Flask-SocketIO',
        'https://github.com/miguelgrinberg/Flask-SocketIO.git',
        'https://docs.aiohttp.org/en/stable/',
        'https://fastapi.tiangolo.com/tutorial/',
        'https://github.com/tiangolo/fastapi.git',
        'https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker.git',
        'https://ya.ru',
    )


def is_valid(url):
    return httpx.get(url).status_code in (200, 301)


def get_github_project(url: str) -> str | None:
    try:
        _, _, domain, _, *remain = url.split('/')
    except ValueError:
        return None
    if domain != DOMAIN or not is_valid(url):
        return None
    return remain[0].split('.')[0]


@decorators.timer
def get_github_projects(urls):
    return [project for project in [get_github_project(url) for url in urls]
            if project is not None]


@decorators.output
def main(title):
    return get_github_projects(__get_test_data())


if __name__ == '__main__':
    main(__doc__)