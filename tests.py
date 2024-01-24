from main import BooksCollector
import pytest


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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_book_empty_genre(self):
        collector = BooksCollector()
        name_book = 'Книга1'

        collector.add_new_book(name_book)

        assert collector.get_book_genre(name_book) == ''

    def test_add_new_book_add_existing_book_one_book_in_dict(self):
        collector = BooksCollector()
        name_book = 'Книга1'

        collector.add_new_book(name_book)
        collector.add_new_book(name_book)

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_long_name_book_not_added_book(self):
        collector = BooksCollector()
        name_book = 'Книга1'
        long_name_book = 'Жизнь, необыкновенные и удивительные приключения Робинзона Крузо'

        collector.add_new_book(name_book)
        collector.add_new_book(long_name_book)

        assert len(collector.get_books_genre()) == 1 and long_name_book not in collector.get_books_genre()

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_correct_genre_addition(self, genre):
        collector = BooksCollector()
        name_book = 'Книга1'

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_book_genre(name_book) == genre

    @pytest.mark.parametrize('genre', ['Fantastic', 'Хоррор', '12414', '!@#$%^', ' '])
    def test_set_book_genre_set_missing_genre_genre_not_add(self, genre):
        collector = BooksCollector()
        name_book = 'Книга1'

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre)

        assert collector.get_book_genre(name_book) == ''

    def test_set_book_genre_name_book_not_in_dist_genre_not_add(self):
        collector = BooksCollector()
        name_book = 'Книга1'
        any_name_book = 'Книга2'

        collector.add_new_book(name_book)
        collector.set_book_genre(any_name_book, 'Детективы')

        assert collector.get_book_genre(name_book) == '' and any_name_book not in collector.get_books_genre()

    def test_get_books_with_specific_genre_add_fantastic_books_get_fantasy_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Комедии')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга1', 'Книга3']

    def test_get_books_for_children_add_books_any_genres_get_books_only_children(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Ужасы')
        collector.add_new_book('Книга3')
        collector.set_book_genre('Книга3', 'Комедии')

        assert collector.get_books_for_children() == ['Книга1', 'Книга3']

    def test_add_book_in_favorites_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')

        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_name_book_not_in_dist_book_not_add_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')

        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')

        assert 'Книга2' not in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_existing_in_favorites_one_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')

        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга1')

        assert 'Книга1' in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_two_books_one_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.add_new_book('Книга2')

        collector.add_book_in_favorites('Книга1')
        collector.add_book_in_favorites('Книга2')

        collector.delete_book_from_favorites('Книга1')

        assert 'Книга2' in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_delete_book_not_in_favorites_list_book_not_delete(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.add_book_in_favorites('Книга1')

        collector.delete_book_from_favorites('Книга2')

        assert 'Книга1' in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 1
