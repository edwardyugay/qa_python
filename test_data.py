# test_data.py

# Тестовые данные для автотестов

# Список книг с жанрами для заполненного коллектора
BOOKS_FOR_TEST = [
    {"name": "Гарри Поттер", "genre": "Фантастика"},
    {"name": "Властелин колец", "genre": "Фантастика"},
    {"name": "1984", "genre": "Фантастика"},
    {"name": "Детектив", "genre": "Детективы"},
    {"name": "Комедия", "genre": "Комедии"}
]

# Валидные имена книг для тестов
BOOK_NAMES_VALID = ["Гарри Поттер", "Властелин колец", "1984"]

# Имена книг, превышающие допустимую длину (более 40 символов)
BOOK_NAMES_TOO_LONG = ["A" * 41, "B" * 50]

# Граничные значения для названия книги
MIN_BOOK_NAME = "A"
MAX_BOOK_NAME = "B" * 40

# Дополнительные тестовые данные для проверки метода get_books_for_children
CHILDREN_FRIENDLY_GENRES = ["Фантастика", "Комедии", "Мультфильмы"]
NON_CHILDREN_FRIENDLY_GENRES = ["Ужасы", "Детективы"]
