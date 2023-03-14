### Здесь лежат два задания:
 - task_1.py - первая задача (алгоритмы)
 - task_2 - второе задание (API)

### Что это за проект?:smiley_cat:
Всё просто: task2 - это бэкенд для сбора информации с WildBerries API (артикул, брэнд, тайтл) + собственный API реализованный на стэке Django Rest Framework+aiohttp+PyDantic. Aiohttp в сочетании с Asyncio позволяет асинхронно обрабатывать запросы к API WildBerries == ускоряет работу приложения.
Интерфейс взаимодействия с сервисом - JSON. После получения ответа от WildBerries также создаётся PyDantic объект.

### Начало взаимодействия с API :old_key:
После [запуска](#как-запустить-проект) проекта, в версии V1 доступен для POST-запросов эндпоинт http://127.0.0.1:8000/api/v1/products/. Получить иноформацию
о продукте можно отправив JSON-(POST)-запрос на [вышеуказанный](http://127.0.0.1:8000/api/v1/products/) эндпоинт. 
Возможны два вида запросов:

1. Отправка единичного артикула:
```
{
"article": "12345"
}
```
Отправлять можно только одно целое число в виде строки или типа integer.

Формат ответа:
```
[
 {
  "article": "12345",
  "brand": "Abidas",
  "title": "Шорты"
 }
]
```

2. Возможна отправка множества артикулов в файле c расширением ".xlsx". Артикулы указываются в первой колонке файла построчно (строго по одному).
Пример запроса с использованием Postman:
- В теле(body) запроса указываем form-data
- В качестве ключа (key) используем file и указываем типа данных (file)
- В графе value выбираем нужный файл с расширением .xlsx
- Отправляем Post-запрос на эндопонит http://127.0.0.1:8000/api/v1/products/

Формат ответа:

```
[
    {
        "article": "73512949",
        "brand": "Мир Фигурного Катания",
        "title": "Аксессуар для коньков"
    },
    {
        "article": "55334425",
        "brand": "MyPads",
        "title": "Чехол-сумочка Borsa a Tracolla для телефона BQ Aqu"
    },
    {
        "article": "56777994",
        "brand": "LotsPrints",
        "title": "Кружка"
    },
    {
        "article": "5555666",
        "brand": "Zia",
        "title": "Юбка"
    }
]
```


### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Artem4es/tasks.git
```

Cоздать и активировать виртуальное окружение:

```
py -m venv venv
```

```
source venv/Scripts/activate (venv/bin/activate для МасOS, Linux)
```

```
python -m pip install --upgrade pip (python3 далее везде для MacOS, Linux)
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```


### This project was created and maintained by [Artem Ezhov](https://github.com/Artem4es)
All rights reserved😆
