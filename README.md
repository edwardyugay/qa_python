# BooksCollector

Проект представляет собой простую библиотеку для сбора и фильтрации книг по жанрам.  
Класс **BooksCollector** реализует следующие возможности:
- Добавление новой книги (ограничение по длине названия: от 1 до 40 символов).
- Назначение жанра книге.
- Получение жанра по имени книги.
- Фильтрация книг по жанрам.
- Получение списка книг, подходящих для детей (с учётом возрастного рейтинга).
- Работа с избранными книгами (добавление, удаление, получение списка).

## Структура проекта

- **main.py** – содержит реализацию класса `BooksCollector`.
- **conftest.py** – файл с фикстурами для тестирования с использованием pytest.
  - `collector` – возвращает новый экземпляр `BooksCollector`.
  - `filled_collector` – возвращает предзаполненный экземпляр `BooksCollector` с данными из модуля `test_data.py`.
- **test_data.py** – модуль с тестовыми данными (набор книг, жанров, граничные значения и др.).
- **tests.py** – набор автотестов, проверяющих работу всех методов класса с использованием тестовых данных.
- **README.md** – данный файл с описанием проекта и инструкциями.

## Установка

1. Клонируйте репозиторий или загрузите файлы проекта.
2. Установите [pytest](https://docs.pytest.org/en/latest/) (если ещё не установлен):

   ```bash
   pip install pytest
