### API для Yatube.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/anign/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

для windows:

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Некоторые примеры запросов к API:

Получить список всех публикаций:

```GET api/v1/posts/```

Создание публикации: 

```POST api/v1/posts/```

Получение публикации по id:

```api/v1/posts/{id}/```
