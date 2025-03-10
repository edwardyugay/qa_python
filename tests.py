import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:
    # Тест добавления новой книги
    def test_add_new_book(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.books_genre
        assert collector.books_genre["Гарри Поттер"] == ""

    # Тест добавления двух книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    # Тест ограничения на длину названия
    @pytest.mark.parametrize("book_name", ["A" * 41, "B" * 50])
    def test_add_new_book_too_long_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    # Тест установки жанра
    @pytest.mark.parametrize("book_name, genre", [("Гарри Поттер", "Фантастика"), ("Детектив", "Детективы")])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест получения жанра
    def test_get_book_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    # Тест получения книг определенного жанра
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер"]

    # Тест получения всех книг
    def test_get_books_genre(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()

    # Тест получения книг для детей
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Детектив")
        collector.set_book_genre("Детектив", "Детективы")
        assert "Гарри Поттер" in collector.get_books_for_children()
        assert "Детектив" not in collector.get_books_for_children()

    # Тест добавления книги в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_list_of_favorites_books()

    # Тест удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    # Тест получения списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]
