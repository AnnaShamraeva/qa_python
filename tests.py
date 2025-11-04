import pytest   
from main import BooksCollector # импортируем класс BooksCollector из файла main


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
      
# 1 Проверка добавления новой книги (add_new_book)
# 1.1 Проверка добавления одной новой книги
    def test_add_new_book_plus_one_book(self): # в имени функции test_ название тестируемого метода указание что тестируем
# self показывает, что этот метод является методом класса
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга ужасов') # добавляем новую книгу
        assert collector.get_books_genre() == {'Новая книга ужасов': ''} # проверяем, что добавилась одна книга

# 1.2 Проверка что нет двойного добавления одной книги 

    def test_add_new_book_add_one_book_two_times_not_possible(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга')
        collector.add_new_book('Новая книга')
        assert collector.get_books_genre() == {'Новая книга': ''} # проверяем, что добавилась одна книга

# 1.3 Проверка добавления новой книги с названием в 0, 41 символ

    @pytest.mark.parametrize('book_name', ['', 'Название книги в 41 символ совсем  просто'])                  
    def test_add_new_book_not_valid_book_name(self, book_name, books_collection):
        books_collection=BooksCollector()
        books_collection.add_new_book(book_name)
        assert len(books_collection.get_books_genre()) == 0    
       

# 1.4 Проверка ГЗ названий книг в 1 и 40 символов.

    @pytest.mark.parametrize('book_name', ['O', 'Название книги в 40 символ совсем просто'])                  
    def test_add_new_book_valid_book_name(self, book_name, books_collection):
        books_collection.add_new_book(book_name)
        assert book_name in books_collection.get_books_genre() 

# 2 Проверка жанра книги  
# 2.1 Проверка валидного жанра если книга есть в словаре books_genre и её жанр входит в список genre.
    
    def test_set_book_genre_valid(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга фантастики')
        collector.set_book_genre('Новая книга фантастики', 'Фантастика')
        assert collector.get_books_genre() == {'Новая книга фантастики': 'Фантастика'}

# 2.2 Проверка невалидного жанра если книга есть в словаре books_genre и её жанр не входит в список genre. 

    def test_set_book_genre_not_valid(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга болтовни')
        collector.set_book_genre('Новая книга болтовни', 'Болтовня')
        assert collector.get_books_genre() == {'Новая книга болтовни': ''}

# 2.3 Проверка валидного жанра если книги нет в словаре books_genre.  

    def test_set_book_genre_book_not_in_book_genre(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.set_book_genre('Новая книга с детективом', 'Детектив')
        assert collector.get_books_genre() == {}

# 3 Проверка получения жанра книги по её имени
    
    def test_get_book_genre_return_genre_set(self):   
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга фантастики')
        collector.set_book_genre('Новая книга фантастики', 'Фантастика')
        assert collector.get_book_genre('Новая книга фантастики') == 'Фантастика'
        # здесь и далее замена создания объекта (экземпляра класса) на использование фикстуры collector через параметр

# 4 Проверка вывода списка книг с определённым жанром

    def test_get_books_with_specific_genre_get_book_by_genre(self):    
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга ужасов')
        collector.set_book_genre('Новая книга ужасов','Ужасы')
        collector.add_new_book('Новая книга ужасов 2')
        collector.set_book_genre('Новая книга ужасов 2','Ужасы')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

# 5 Проверка получения книг для детей
     
    def test_get_books_for_children_get_book_without_age_rating_possible(self, random_book):
        assert len(random_book.get_books_for_children()) == 3

# 6 Проверка добавления книги в Избранное
# 6.1 Проверка добавления книги в Избранное

    def test_add_book_in_favorites_add_new_book_possible(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга ужасов')
        collector.set_book_genre('Новая книга ужасов','Ужасы')
        collector.add_book_in_favorites('Новая книга ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1

# 6.2 Проверка двойного добавления книги в Избранное

    def test_add_book_in_favorites_add_one_book_two_times_not_possible(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга ужасов')
        collector.set_book_genre('Новая книга ужасов','Ужасы')
        collector.add_book_in_favorites('Новая книга ужасов')
        collector.add_book_in_favorites('Новая книга ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1

# 7 Проверка удаления книги из Избранного

    def test_delete_book_from_favorites_delete_book_possible(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_book_in_favorites('Новая книга ужасов')
        collector.set_book_genre('Новая книга ужасов','Ужасы')
        collector.delete_book_from_favorites('Новая книга ужасов')
        favorites = collector.get_list_of_favorites_books()
        assert 'Новая книга ужасов' not in favorites

# 8 Проверка получения списка Избранных книг

    def test_get_list_of_favorites_books_get_list_of_favorites_books_successful(self):
        collector = BooksCollector() # создаем объект класса BooksCollector
        collector.add_new_book('Новая книга ужасов')
        collector.set_book_genre('Новая книга ужасов','Ужасы')
        collector.add_book_in_favorites('Новая книга ужасов')
        assert len(collector.get_list_of_favorites_books()) == 1