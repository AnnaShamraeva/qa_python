Unit-тесты для приложения BooksCollector. Оно позволяет установить жанр книг и добавить их в избранное.

Класс BooksCollector содержит:
Словарь books_genre, куда можно добавить пару Название книги: Жанр книги.
Список favorites, который содержит избранные книги.
Список genre, который содержит доступные жанры.
Список genre_age_rating, который содержит жанры с возрастным рейтингом.

Набор методов для работы со словарем books_genre и списком favorites:

1. add_new_book — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз. Покрыт тестами 1.1 Проверка добавления одной новой книги,  1.2 Проверка что нет двойного добавления одной книги и 1.3 Проверка добавления новой книги с названием в 0, 41 символ. Проверка добавления книги с допустимой длинной названия в тесте 1.1 и 1.4 Проверка ГЗ названий книг в 1 и 40 символов.

2. set_book_genre — устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre. Покрвыается тестами 2.1 Проверка валидного жанра если книга есть в словаре books_genre и её жанр входит в список genre и 2.2 Проверка невалидного жанра если книга есть в словаре books_genre и её жанр не входит в список genre. 

3. get_book_genre — выводит жанр книги по её имени. Покрыт тестом номер 3 Проверка получения жанра книги по её имени

4. get_books_with_specific_genre — выводит список книг с определённым жанром. Покрыт тестом номер 4 Проверка вывода списка книг с определённым жанром

5. get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга. Покрыт тестом 5 Проверка получения книг для детей

6. add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
Метод покрыт тестами 6.1 Проверка добавления книги в Избранное и 6.2 Проверка двойного добавления книги в Избранное

7. delete_book_from_favorites — удаляет книгу из избранного, если она там есть. Покрыт 9 Проверка удаления книги из Избранного

8. get_list_of_favorites_books — получает список избранных книг. Покрыт 8 Проверка получения списка Избранных книг

Для тестов написаны две фикстуры. Они вынесены в отдельный файл conftest.py

Проведено 16 тестов: 16 passed in 0.11s
Все методы покрыты тестами.

platform win32 -- Python 3.12.10, pytest-8.4.2, pluggy-1.6.0 -- C:\Users\anna_\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe
cachedir: .pytest_cache
rootdir: C:\my_first_vscode_project
collected 16 items                                                                                                                                              

qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_new_book_plus_one_book PASSED                                                                  [  6%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_new_book_add_one_book_two_times_not_possible PASSED                                            [ 12%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_new_book_not_valid_book_name[] PASSED                                                          [ 18%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_new_book_not_valid_book_name[\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438 \u0432 41 \u0441\u0438\u043c\u0432\u043e\u043b \u0441\u043e\u0432\u0441\u0435\u043c  \u043f\u0440\u043e\u0441\u0442\u043e] PASSED [ 25%]
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_new_book_valid_book_name[O] PASSED                                                             [ 31%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_new_book_valid_book_name[\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043d\u0438\u0433\u0438 \u0432 40 \u0441\u0438\u043c\u0432\u043e\u043b \u0441\u043e\u0432\u0441\u0435\u043c \u043f\u0440\u043e\u0441\u0442\u043e] PASSED [ 37%]
qa_python_4/qa_python/tests.py::TestBooksCollector::test_set_book_genre_valid PASSED                                                                        [ 43%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_set_book_genre_not_valid PASSED                                                                    [ 50%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_set_book_genre_book_not_in_book_genre PASSED                                                       [ 56%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_get_book_genre_return_genre_set PASSED                                                             [ 62%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_get_books_with_specific_genre_get_book_by_genre PASSED                                             [ 68%]
qa_python_4/qa_python/tests.py::TestBooksCollector::test_get_books_for_children_get_book_without_age_rating_possible PASSED                                 [ 75%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_book_in_favorites_add_new_book_possible PASSED                                                 [ 81%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_add_book_in_favorites_add_one_book_two_times_not_possible PASSED                                   [ 87%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_delete_book_from_favorites_delete_book_possible PASSED                                             [ 93%] 
qa_python_4/qa_python/tests.py::TestBooksCollector::test_get_list_of_favorites_books_get_list_of_favorites_books_successful PASSED   





