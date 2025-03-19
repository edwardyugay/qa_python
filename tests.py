# tests.py
import pytest
from main import BooksCollector
from test_data import (
    BOOK_NAMES_VALID,
    BOOK_NAMES_TOO_LONG,
    MIN_BOOK_NAME,
    MAX_BOOK_NAME,
    NON_CHILDREN_FRIENDLY_GENRES,
)

class TestBooksCollector:
    # Тест добавления новой книги с разными именами
    @pytest.mark.parametrize("book_name", BOOK_NAMES_VALID)
    def test_add_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre
        assert collector.books_genre[book_name] == ""

    # Тест добавления двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    # Тест добавления дублирующейся книги
    def test_add_duplicate_book(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Гарри Поттер")
        assert len(collector.get_books_genre()) == 1

    # Тест ограничения на длину названия: более 40 символов не добавляются
    @pytest.mark.parametrize("book_name", BOOK_NAMES_TOO_LONG)
    def test_add_new_book_too_long_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    # Тест границ: название книги с 1 и 40 символами добавляются
    def test_add_new_book_boundary_names(self, collector):
        collector.add_new_book(MIN_BOOK_NAME)
        collector.add_new_book(MAX_BOOK_NAME)
        assert MIN_BOOK_NAME in collector.books_genre
        assert MAX_BOOK_NAME in collector.books_genre

    # Тест установки жанра
    @pytest.mark.parametrize("book_name, genre", [("Гарри Поттер", "Фантастика"), ("Детектив", "Детективы")])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест установки недопустимого жанра
    def test_set_invalid_book_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Несуществующий жанр")
        # Жанр должен остаться пустым, если введён недопустимый жанр
        assert collector.get_book_genre("Гарри Поттер") == ""

    # Тест получения жанра книги без установки жанра (значение по умолчанию)
    def test_get_book_genre_default(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert collector.get_book_genre("Гарри Поттер") == ""
        # Для не добавленной книги возвращается None
        assert collector.get_book_genre("Неизвестная книга") is None

    # Тест получения книг определённого жанра при наличии нескольких вариантов
    def test_get_books_with_specific_genre(self, collector):
        # Добавляем книги
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Властелин колец")
        collector.add_new_book("1984")
        collector.add_new_book("Гордость и предубеждение")
        # Устанавливаем жанры
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Властелин колец", "Фантастика")
        collector.set_book_genre("1984", "Фантастика")
        collector.set_book_genre("Гордость и предубеждение", "Детективы")
        expected_books = ["Гарри Поттер", "Властелин колец", "1984"]
        assert collector.get_books_with_specific_genre("Фантастика") == expected_books

    # Тест получения списка книг, когда список пуст
    def test_get_books_genre_empty(self, collector):
        assert collector.get_books_genre() == {}

    # Тест получения книг для детей (индивидуально)
    @pytest.mark.parametrize("book_name, genre", [("Гарри Поттер", "Фантастика"), ("Детектив", "Детективы")])
    def test_get_books_for_children_individual(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        if genre in NON_CHILDREN_FRIENDLY_GENRES:
            assert book_name not in collector.get_books_for_children()
        else:
            assert book_name in collector.get_books_for_children()

    # Тест получения книг для детей с несколькими книгами (используя filled_collector)
    def test_get_books_for_children_multiple(self, filled_collector):
        # Из filled_collector ожидаем, что книги "Гарри Поттер", "Властелин колец",
        # "1984" и "Комедия" подходят для детей, а "Детектив" – нет.
        children_books = filled_collector.get_books_for_children()
        assert "Гарри Поттер" in children_books
        assert "Властелин колец" in children_books
        assert "1984" in children_books
        assert "Комедия" in children_books
        assert "Детектив" not in children_books

    # Тест добавления книги в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        # Повторное добавление не должно создать дубликат
        collector.add_book_in_favorites("Гарри Поттер")
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["Гарри Поттер"]

    # Тест удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    # Тест удаления книги, которой нет в избранном
    def test_delete_nonexistent_book_from_favorites(self, collector):
        collector.delete_book_from_favorites("Неизвестная книга")
        # Список избранного должен оставаться пустым
        assert collector.get_list_of_favorites_books() == []

    # Тест получения списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]

    # Тест получения списка избранных книг, когда список пуст
    def test_get_list_of_favorites_books_empty(self, collector):
        assert collector.get_list_of_favorites_books() == []
