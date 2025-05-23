### Отчет по лабораторной работе: Реализация параметризованного декоратора для логирования

#### Введение

В данной лабораторной работе основной целью было создание параметризованного декоратора для логирования вызовов функций. Это позволило мне изучить, как работают декораторы в Python, а также научиться эффективно организовывать логирование данных в различных форматах: консоль, JSON и SQLite. Этот опыт помог мне лучше понять гибкость Python в обработке данных и разбиение задач на более мелкие и управляемые компоненты.

### Описание задачи

Задача заключалась в разработке декоратора `trace`, который выполняет логирование вызовов функций в различных форматах:

1. По умолчанию логирует данные в консоль.
2. Может записывать логи в JSON-файл, если в параметре передано имя файла с расширением `.json`.
3. Может сохранять логи в базе данных SQLite, если передан объект типа `sqlite3.Connection`.

Для выполнения задания я реализовал несколько вспомогательных декораторов, а также утилиту `showlogs`, которая позволяет просматривать содержимое логов из базы данных SQLite.

### Реализация

#### 1. Реализация декоратора `trace` для логирования в консоль

Для начала я создал базовый декоратор `trace`, который по умолчанию выводит информацию о вызовах функций в консоль. Это позволило мне изучить структуру декоратора и разобраться, как происходит перехват вызова функции и логирование информации.

Пример использования:
```python
@trace(handle=sys.stdout)
def example_function(x):
    return x * 2

example_function(5)
```

#### 2. Логирование в JSON-файл

Следующим шагом было добавление возможности записи логов в JSON-файл. Для этого я создал декоратор `log_to_json`, который сериализует данные о вызове функции в формате JSON и записывает их в указанный файл. Это позволило сохранить логи между запуском программы и эффективно анализировать их позже.

Пример использования:
```python
@trace(handle="logger.json")
def cube(x):
    return x ** 3

cube(3)
```

Пример записи в `logger.json`:
```json
{
    "datetime": "2025-04-10T12:31:40.258123",
    "func_name": "cube",
    "params": [3],
    "result": 27
}
```

#### 3. Логирование в базу данных SQLite

Для записи логов в базу данных SQLite я использовал модуль `sqlite3`. Создание таблицы и запись данных в нее выполнялись с помощью SQL-запросов. Я также добавил проверку на существование таблицы, чтобы избежать ошибок при повторных вызовах декоратора.

Пример использования:
```python
import sqlite3

handle = sqlite3.connect(":memory:")

@trace(handle=handle)
def power_four(x):
    return x ** 4

power_four(2)
```

Для просмотра логов из базы данных я создал утилиту `showlogs`:
```python
showlogs(handle)
```

Вывод:
```python
(1, '2025-04-10T12:31:40.258457', 'power_four', '2', '16')
```

#### 4. Использование контекстного менеджера для управления ресурсами

Для управления ресурсами базы данных я использовал контекстный менеджер `doc`, который автоматически создает и закрывает соединение с базой данных, а также освобождает память после выполнения работы с ней.

Пример использования:
```python
with doc() as handle:
    @log_to_sqlite(handle)
    def f4(x):
        return x ** 4
    f4(3)
    f4(5)
    showlogs(handle)
```

#### 5. Объединение всех компонентов

В финальной реализации я использовал все три типа логирования (в консоль, в JSON и в SQLite), создав декораторы с параметрами. Также я создал вспомогательные функции для просмотра логов и работы с памятью.

### Полезные выводы

1. **Параметризованные декораторы**: Создание параметризованного декоратора `trace` дало мне понимание, как можно делать декораторы более гибкими и настраиваемыми через параметры, такие как `handle`.
2. **Работа с базами данных**: Изучение SQLite позволило мне освоить основные принципы работы с базами данных в Python, включая создание таблиц и выполнение SQL-запросов.
3. **Логирование**: Я научился организовывать логирование данных в различных форматах, что может быть полезно для отладки и мониторинга работы программы.
4. **Гибкость Python**: Python предоставил мне мощные инструменты для работы с различными форматами данных (JSON, SQLite) и для организации логирования, что сделало задачу более интересной и познавательной.

### Заключение

В этой лабораторной работе я изучил, как эффективно использовать декораторы для логирования функций в различных форматах. Я научился работать с JSON, SQLite и контекстными менеджерами, что значительно расширило мои знания о Python. Этот опыт был полезен для улучшения навыков в программировании и обработки данных, а также для более глубокого понимания принципов работы с функциями и их декорированием.
