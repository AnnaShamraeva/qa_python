from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


# 1 Проверка добавления новой книги

    def test_add_new_book_plus_one_book(self): # в имени функции test_ название тестируемого метода указание что тестируем
# self показывает, что этот метод является методом класса
        collector =  BooksCollector() # создаем экземпляр класса BookCollector
        collector.add_new_book('Новая книга ужасов') # добовляем новую книгу
        assert len(collector.get_books_genre()) == 1
            
# 2 Проверка жанра книги  

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
# с помощью @pytest.mark.parametrize тест будет выполнен для каждого жанра из списка 
    def test_init_all_genre_exist(self, genre):
        collector = BooksCollector() # в каждом запуске создаем экземпляр класса BookCollector
        assert genre in collector.genre # проверяем жанр на наличие в списке genre

# 3 Проверка присвоения жанра книги по её имени
# 3.1 Жанр из списка

    def test_set_book_genre_from_list_set_possible(self):
        collector = BooksCollector() # создаем экземпляр класса BookCollector
        collector.add_new_book('Новая книга ужасов') # добавляем новую книгу
        collector.set_book_genre('Новая книга ужасов', 'Ужасы') # метод set_book_genre задает книге жанр
        assert collector.get_books_genre('Новая книга ужасов') == 'Ужасы' # проверка что жанр присвоен правильно

# 3.2 Жанр не из списка

    def test_get_book_genre_from_not_in_list_set_possible(self): 
        collector = BookCollector()  # создаем экземпляр класса BookCollector
        collector.add_new_book('Новая книга комиксов') # добавляем новую книгу
        collector.set_book_genre('Новая книга комиксов', 'Комиксы') # метод set_book_genre задает книге жанр
        assert collector.get_book_genre('Новая книга комиксов') == '' # проверка что жанр присвоен правильно

# 4 Проверка получения жанра книги по её имени
    
    def test_get_book_genre_return_genre_set(self, collector_book):   
        assert collector_book.get_books_genre('Новая книга ужасов') == 'Ужасы'

# 5 Проверка вывода списка книг с определённым жанром

    def get_books_with_specific_genre_get_book_by_genre(self, collector_book):    
        assert len(collector_book.get_books_with_specific_genre('Ужасы')) == 1

# 6 Проверка получения книг для детей
     
    def test_get_books_for_children_get_book_without_age_rating_possible(self, collector_book):
        assert len(collector_book.get_books_for_children()) == 1

# 7 Проверка добавления книги в Избранное
# 7.1 Проверка добавления книги в Избранное

    def add_book_in_favorites_add_new_book_possible(self, collector_book):
        collector_book.add_book_in_favorites('Новая книга ужасов')
        assert len(collector_book.get_list_of_favorites_books()) == 1

# 7.2 Проверка двойного добавления книги в Избранное

    def add_book_in_favorites_add_one_book_two_times_not_possible(self, collector_book):
        collector_book.add_book_in_favorites('Новая книга ужасов')
        collector_book.add_book_in_favorites('Новая книга ужасов')
        assert len(collector_book.get_list_of_favorites_books()) == 1

# 8 Проверка удаления книги из Избранного

    def test_delete_book_from_favorites_delete_book_possible(self, collector_book):
        collector_book.add_book_in_favorites('Новая книга ужасов')
        collector_book.delete_book_in_favorites('Новая книга ужасов')
        favorites = collector_book.get_list_of_favorites_books()
        assert 'Новая книга ужасов' not in favorites

# 9 Проверка получения списока Избранных книг

    def test_get_list_of_favorites_books_get_list_of_favorites_books_successful(self, collector_book):
        collector_book.add_book_in_favorites('Новая книга ужасов')
        assert len(collector_book.get_list_of_favorites_books()) == 1