import pytest # импортируем библиотеку pytest
from main import BooksCollector # импортируем класс BooksCollector из файла main


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture # создаем функцию для создания тестовых объектов в начале тестов после класса 
    def collector(self):
        return BooksCollector() # в каждом запуске создаем экземпляр класса BooksCollector
         
# 1 Проверка добавления новой книги

    def test_add_new_book_plus_one_book(self, collector): # в имени функции test_ название тестируемого метода указание что тестируем
# self показывает, что этот метод является методом класса
        collector.add_new_book('Новая книга ужасов') # добавляем новую книгу
        assert len(collector.get_books_genre()) == 1 # проверяем, что добавилась одна книга
            
# 2 Проверка жанра книги  
# 2.1 Проверка валидного жанра книги
    
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
# с помощью @pytest.mark.parametrize тест будет выполнен для каждого жанра из списка 
    def test_init_all_genre_exist(self, collector, genre):
        assert genre in collector.genre # проверяем жанр на наличие в списке genre

# 2.2 Проверка невалидного жанра книги

    @pytest.mark.parametrize('invalid_genre', ['Комиксы', ' ', '666', None])
    def test_init_all_genre_is_invalid(self, collector, invalid_genre):
        collector.set_book_genre('Книга', invalid_genre)
        assert collector.get_books_genre('Книга') != invalid_genre

# 3 Проверка присвоения жанра книги по её имени
# 3.1 Жанр из списка

    def test_set_book_genre_from_list_set_possible(self, collector):
        collector.add_new_book('Новая книга ужасов') # добавляем новую книгу
        collector.set_book_genre('Новая книга ужасов', 'Ужасы') # метод set_book_genre задает книге жанр
        assert collector.get_books_genre('Новая книга ужасов') == 'Ужасы' # проверка что жанр присвоен правильно

# 3.2 Жанр не из списка 

    def test_get_book_genre_from_not_in_list_set_possible(self, collector): 
        collector.add_new_book('Новая книга комиксов') # добавляем новую книгу
        collector.set_book_genre('Новая книга комиксов', 'Комиксы') # метод set_book_genre задает книге жанр
        assert collector.get_books_genre('Новая книга комиксов') == '' # проверка что жанр присвоен правильно

# 4 Проверка получения жанра книги по её имени
    
    def test_get_book_genre_return_genre_set(self, collector):   
        assert collector.get_books_genre('Новая книга ужасов') == 'Ужасы'
        # здесь и далее замена создания объекта (экземпляра класса) на использование фикстуры collector через параметр

# 5 Проверка вывода списка книг с определённым жанром

    def test_get_books_with_specific_genre_get_book_by_genre(self, collector):    
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 1

# 6 Проверка получения книг для детей
     
    def test_get_books_for_children_get_book_without_age_rating_possible(self, collector):
        assert len(collector.get_books_for_children()) == 1

# 7 Проверка добавления книги в Избранное
# 7.1 Проверка добавления книги в Избранное

    def test_add_book_in_favorites_add_new_book_possible(self, collector):
        collector.add_book_in_favorites('Новая книга ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1

# 7.2 Проверка двойного добавления книги в Избранное

    def test_add_book_in_favorites_add_one_book_two_times_not_possible(self, collector):
        collector.add_book_in_favorites('Новая книга ужасов')
        collector.add_book_in_favorites('Новая книга ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1

# 8 Проверка удаления книги из Избранного

    def test_delete_book_from_favorites_delete_book_possible(self, collector):
        collector.add_book_in_favorites('Новая книга ужасов')
        collector.delete_book_in_favorites('Новая книга ужасов')
        favorites = collector.get_list_of_favorites_books()
        assert 'Новая книга ужасов' not in favorites

# 9 Проверка получения списка Избранных книг

    def test_get_list_of_favorites_books_get_list_of_favorites_books_successful(self, collector):
        collector.add_book_in_favorites('Новая книга ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1