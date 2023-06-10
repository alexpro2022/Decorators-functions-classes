# Питонические игры от Андрея Пронина
Тестовые задания для соискателя 1 этап

<br>

## Оглавление:
- [Технологии](#технологии)
- [Описание работы](#описание-работы)
- [Установка и запуск](#установка-и-запуск)
- [Удаление](#удаление)
- [Автор](#автор)

<br>

## Технологии:

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)](https://www.python.org/)
[![asyncio](https://img.shields.io/badge/-asyncio-464646?logo=python)](https://docs.python.org/3/library/asyncio.html)
[![aiohttp](https://img.shields.io/badge/-aiohttp-464646?logo=aiohttp)](https://docs.aiohttp.org/en/stable/index.html)
[![httpx](https://img.shields.io/badge/-httpx-464646?logo=httpx)](https://www.python-httpx.org/)

[⬆️Оглавление](#оглавление)

<br>

## Описание работы:
Тестовые задания для соискателя 1 этап - реализация функций и классов.
<details><summary>Подробнее</summary>
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
### Для удобства запуск производится в Docker-контейнере.
1. Клонируйте репозиторий с GitHub:
```bash
git clone https://github.com/alexpro2022/Pythonic-games-1-stage.git && cd Pythonic-games-1-stage 
```

<details><summary>Запуск одним файлом (согласно ТЗ)</summary>
    
2. Из корневой директории проекта выполните команду:

```bash
cd group_run && docker build -t image . && docker run image && cd ..
```  
<h1></h1>
</details>

<details><summary>Индивидуальный запуск</summary>

2. Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок на проекты на гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO, https://github.com/miguelgrinberg/Flask-SocketIO.git). Функция должна обработать полученные ссылки и вывести в консоль названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".
```bash
cd individual_run/github_links && docker build -t image . && docker run image && cd ../..
```

3. Реализовать функцию, принимающую два списка и возвращающую словарь (ключ из первого списка, значение из второго), упорядоченный по ключам. Результат вывести в консоль. Длина первого списка не должна быть равна длине второго. Результат вывести в консоль.
```bash
cd individual_run/create_dict && docker build -t image . && docker run image && cd ../..
```

4. Реализовать функцию с помощью методов map и lambda. Функция принимает список элементов (состоящий из строк и цифр), возвращает новый список, с условием - если элемент списка был строкой, в начало строки нужно добавить текст "abc_", в конец строки - "_cba". Если элемент был int - то его значение нужно возвести в квадрат. Результат вывести в консоль.
```bash
cd individual_run/new_list && docker build -t image . && docker run image && cd ../..
```

5. Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу: http://httpbin.org/delay/3. Запросы должны выполняться асинхронно. Допускается написание вспомогательных функций и использование сторонних библиотек. Результат замера времени выводит в консоль. Ожидаемое время не должно превышать 10 секунд.
```bash
cd individual_run/timer && docker build -t image . && docker run image && cd ../..
```

6. Написать класс, принимающий на вход текст. Один метод класса должен выводить в консоль самое длинное слово в тексте. Второй метод - самое часто встречающееся слово. Третий метод выводит количество спецсимволов в тексте (точки, запятые и так далее). Четвертый метод выводит все палиндромы через запятую. Написать декоратор к предыдущему классу, который будет выводить в консоль время выполнения каждого метода. Результат выполнения задания должен быть оформлен в виде файла с кодом.
```bash
cd individual_run/text_class && docker build -t image . && docker run image && cd ../..
```
<h1></h1>

[⬆️Оглавление](#оглавление)    
</details>

<br>

## Удаление:
Для удаления проекта выполните команду:
```bash
cd .. && rm -fr Pythonic-games-1-stage && deactivate
```
  
[⬆️Оглавление](#оглавление)

<br>

## Автор:
[Aleksei Proskuriakov](https://github.com/alexpro2022)

[⬆️В начало](#Питонические-игры-от-Андрея-Пронина)


