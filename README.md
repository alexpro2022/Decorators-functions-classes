# Декораторы, функции и классы
[![Test Suite](https://github.com/alexpro2022/Decorators-functions-classes/actions/workflows/main.yml/badge.svg)](https://github.com/alexpro2022/Decorators-functions-classes/actions/workflows/main.yml)

#### Тестовые задания - реализация декораторов, функций и классов.

<br>

## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![aiohttp](https://img.shields.io/badge/-aiohttp-464646?logo=aiohttp)](https://docs.aiohttp.org/en/stable/index.html)
[![httpx](https://img.shields.io/badge/-httpx-464646?logo=httpx)](https://www.python-httpx.org/)

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:
<details><summary>Подробнее</summary><br>
Все решения нужно поместить в один репозиторий, в нем же подготовить тестовые данные. Для проверки должно быть достаточно запустить один файл.
    <h1></h1>
  A. Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок на проекты на гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git). Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".
    <h1></h1>
  B. Реализовать функцию, принимающую два списка и возвращающую словарь (ключ из первого списка, значение из второго), упорядоченный по ключам. Результат вывести в консоль. Длина первого списка не должна быть равна длине второго. Результат вывести в консоль.
    <h1></h1>
  C. Реализовать функцию с помощью методов map и lambda. Функция принимает список элементов (состоящий из строк и цифр), возвращает новый список, с условием - если элемент списка был строкой, в начало строки нужно добавить текст "abc_", в конец строки - "_cba". Если элемент был int - то его значение нужно возвести в квадрат. Результат вывести в консоль.
    <h1></h1>
  D. Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу: http://httpbin.org/delay/3. Запросы должны выполняться асинхронно. Допускается написание вспомогательных функций и использование сторонних библиотек. Результат замера времени выводит в консоль. Ожидаемое время не должно превышать 10 секунд.
    <h1></h1>
  E. Написать класс, принимающий на вход текст. Один метод класса должен выводить в консоль самое длинное слово в тексте. Второй метод - самое часто встречающееся слово. Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее). Четвертый метод выводит все палиндромы через запятую.
    <h1></h1>
  F. Написать декоратор к предыдущему классу, который будет выводить в консоль время выполнения каждого метода. Результат выполнения задания должен быть оформлен в виде файла с кодом.
    <h1></h1>

[⬆️Оглавление](#оглавление)
</details>

<br>

## Установка и запуск:
Удобно использовать принцип copy-paste - копировать команды из GitHub Readme и вставлять в командную строку Git Bash или IDE (например VSCode).

1. Клонируйте репозиторий с GitHub:
```bash
git clone https://github.com/alexpro2022/Decorators-functions-classes.git && cd Decorators-functions-classes

```

<details><summary>Запуск в Docker</summary><br>

<details><summary>Предварительные условия для Docker</summary>

Предполагается, что пользователь установил [Docker](https://docs.docker.com/engine/install/). 
Проверить наличие можно выполнив команды:

```bash
docker --version && docker-compose --version
```

</details>
    
2. Запустите приложение в docker-контейнере:
```bash
docker build -t image . && docker run image
```
<h1></h1>
</details>

<details><summary>Запуск в виртуальном окружении</summary><br>

2. Создайте и активируйте виртуальное окружение:
   * Если у вас Linux/macOS
   ```bash
    python -m venv venv && source venv/bin/activate
   ```
   * Если у вас Windows
   ```bash
    python -m venv venv && source venv/Scripts/activate
   ```

3. Установите в виртуальное окружение зависимости:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```

<details><summary>Запуск одним файлом</summary><br>

```bash
python main.py
```
<h1></h1>
</details>

<details><summary>Индивидуальный запуск функций</summary><br>

A. Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок на проекты на гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git). Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".
```bash
python functions/github_links.py 
```

B. Реализовать функцию, принимающую два списка и возвращающую словарь (ключ из первого списка, значение из второго), упорядоченный по ключам. Результат вывести в консоль. Длина первого списка не должна быть равна длине второго. Результат вывести в консоль.
```bash
python functions/create_dict.py 
```

C. Реализовать функцию с помощью методов map и lambda. Функция принимает список элементов (состоящий из строк и цифр), возвращает новый список, с условием - если элемент списка был строкой, в начало строки нужно добавить текст "abc_", в конец строки - "_cba". Если элемент был int - то его значение нужно возвести в квадрат. Результат вывести в консоль.
```bash
python functions/new_list.py 
```

D. Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу: http://httpbin.org/delay/3. Запросы должны выполняться асинхронно. Допускается написание вспомогательных функций и использование сторонних библиотек. Результат замера времени выводит в консоль. Ожидаемое время не должно превышать 10 секунд.
```bash
python functions/hundred_requests.py 
```

E. Написать класс, принимающий на вход текст. Один метод класса должен выводить в консоль самое длинное слово в тексте. Второй метод - самое часто встречающееся слово. Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее). Четвертый метод выводит все палиндромы через запятую. Написать декоратор к предыдущему классу, который будет выводить в консоль время выполнения каждого метода. Результат выполнения задания должен быть оформлен в виде файла с кодом.
```bash
python functions/text_class.py 
```
<h1></h1>
</details>

[⬆️Оглавление](#оглавление)    
</details>

<br>

## Удаление:
Из корневой директории проекта выполните команду:
```bash
cd .. && rm -fr Decorators-functions-classes && deactivate
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Декораторы-функции-и-классы)


