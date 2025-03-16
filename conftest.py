# conftest.py
import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    """Возвращает новый объект BooksCollector."""
    return BooksCollector()

@pytest.fixture
def filled_collector():
    """
    Возвращает BooksCollector с предзаполненными данными,
    используя тестовые данные из test_data.py.
    """
    from test_data import BOOKS_FOR_TEST

    coll = BooksCollector()
    for book in BOOKS_FOR_TEST:
        coll.add_new_book(book["name"])
        coll.set_book_genre(book["name"], book["genre"])
    return coll
