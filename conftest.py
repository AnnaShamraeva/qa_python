import pytest # импортируем библиотеку pytest
from main import BooksCollector # импортируем класс BooksCollector из файла main

@pytest.fixture # декаратор
def books_collection():
    books_collection=BooksCollector() # создает новый экземпляр BooksCollector когда тест запрашивает фикстуру с именем books_collection
    return books_collection # имя фикстуры должно быть указано как параметр тестовой функции