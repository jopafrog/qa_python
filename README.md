# qa_python

### Список тестов:
- test_add_new_book_add_two_books - проверка добавления книг в словарь
- test_add_new_book_add_book_empty_genre - проверка заполнения ключа genre при добавлении книги в словарь
- test_add_new_book_add_existing_book_one_book_in_dict - негативная проверка на добавление книги, которая уже есть в словаре
- test_add_new_book_long_name_book_not_added_book - негативная проверка добавления книги с названием, длиннее 41 символа
- test_set_book_genre_correct_genre_addition - проверка присвоения жанра книге из списка жанров
- test_set_book_genre_set_missing_genre_genre_not_add - негативная проверка на присвоение жанра книге, которых нет в списке
- test_set_book_genre_name_book_not_in_dist_genre_not_add - негативная проверка присвоение жанра книге, которой нет в словаре
- test_get_books_with_specific_genre_add_fantastic_books_get_fantasy_books - проверка вывода списка книг по жанру Фантастика
- test_get_books_for_children_add_books_any_genres_get_books_only_children - проверка вывода списка книг, подходящих для детей
- test_add_book_in_favorites_add_two_books - проверка добавления книг в список избранных
- test_add_book_in_favorites_name_book_not_in_dist_book_not_add_favorites - негативная проверка добавления книги в Избранное, которой нет в словаре
- test_add_book_in_favorites_book_existing_in_favorites_one_book_in_favorites - негативная проверка добавления книги в Избранное, которая уже есть в списке Избранных
- test_delete_book_from_favorites_two_books_one_book_in_favorites - проверка удаления книги из Избранного
- test_delete_book_from_favorites_delete_book_not_in_favorites_list_book_not_delete - негативная проверка удаления книги из списка Избранное, которой нет в этом списке

Методы класса BooksCollector, такие как: get_books_genre(), get_list_of_favorites_books() - проверяются внутри вышеописанных тестов
