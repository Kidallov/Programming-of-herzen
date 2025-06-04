# Отчёт по лабораторной работе

## Разработка REST API с FastAPI, SQLModel и Docker

## Цель работы

* Получение списка всех терминов.
* Получение информации о конкретном термине по ключевому слову.
* Добавление нового термина с описанием.
* Обновление существующего термина.
* Удаление термина из глоссария.
* Использование Pydantic для валидации входных данных и формирования схем.

## Описание проекта

Реализован REST API для управления глоссарием терминов с использованием FastAPI и SQLModel.
Все модели данных построены на основе Pydantic, что обеспечивает автоматическую валидацию данных и генерацию схем.

## Технологии

* Python 3.12
* FastAPI — веб-фреймворк для создания API
* SQLModel — ORM с поддержкой Pydantic
* MySQL — база данных
* Docker и docker-compose — для контейнеризации и оркестрации
* Nginx — обратный прокси

## Ключевые компоненты проекта

### Основные модели (Pydantic + SQLModel)

```python
from pydantic import BaseModel
from sqlmodel import SQLModel, Field

# Pydantic модель для валидации валюты (пример)
class Valute(BaseModel):
    name: str
    time_n_date: Union[str, None] = ""
    value: float

# SQLModel модель для термина (таблица в БД)
class Term(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    description: str = Field(default="")
```

### CRUD операции

* **GET /terms** — получить список всех терминов
* **GET /terms/{term\_name}** — получить термин по имени
* **POST /terms** — создать новый термин (валидация с помощью Pydantic)
* **PUT /terms/{term\_name}** — обновить описание термина
* **DELETE /terms/{term\_name}** — удалить термин

## Работа с базой данных

* Подключение к MySQL через SQLAlchemy URL `mysql+mysqlconnector://...`
* Автоматическое создание таблиц при запуске сервиса
* Использование сессий SQLModel для работы с данными

## Запуск приложения

1. Построить и запустить контейнеры с помощью docker-compose:

```bash
docker-compose up --build
```

2. Перейти в браузер по адресу `http://localhost/`
3. Использовать Swagger UI по адресу `http://localhost/docs` для тестирования API.

## Результаты

* Все цели работы выполнены.
* Входящие данные валидируются с помощью Pydantic.
* API работает стабильно, поддерживает полный цикл CRUD.
* Сервис контейнеризован и использует nginx для обратного проксирования.

