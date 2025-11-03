import pytest # импортируем библиотеку pytest
from main import BooksCollector # импортируем класс BooksCollector из файла main

@pytest.fixture # декаратор
def books_collection():
    books_collection=BooksCollector() # создает новый экземпляр BooksCollector когда тест запрашивает фикстуру с именем books_collection
    return books_collection # имя фикстуры должно быть указано как параметр тестовой функции

@pytest.fixture
def random_book(books_collection):
    random_book = books_collection
    title = ['Тестовая книга фантастики', 'Тестовая книга ужасов', 'Тестовая книга с детективами', 'Тестовая книга про мультфильмы', 'Тестовая книга комедий']
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    for i in range(5):
        random_book.add_new_book(title[i])
        random_book.set_book_genre(title[i], genre[i])
    return random_book