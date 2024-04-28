from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Pyhton')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['LotR: Fellowship of the Pyhton and how they miss Boromir', ''])
    def test_add_new_book_add_book_with_42_symbols_in_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_add_genre_to_book(self, genre):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', genre)
        assert collector.books_genre['LotR: Fellowship of the Python'] == genre

    def test_set_book_genre_incorrect_genre_name(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Стендап')
        assert collector.books_genre['LotR: Fellowship of the Python'] == ''

    def test_get_book_genre_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        assert collector.get_book_genre('LotR: Fellowship of the Python') == 'Фантастика'

    def test_get_books_with_specific_genre_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        collector = BooksCollector()
        collector.add_new_book('LotR: Return of the Snake King')
        collector.set_book_genre('LotR: Return of the Snake King', 'Ужасы')
        collector.add_new_book('LotR: Return of the Python King')
        collector.set_book_genre('LotR: Return of the Python King', 'Ужасы')
        assert ['LotR: Return of the Snake King',
                'LotR: Return of the Python King'] == collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_genre_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        assert collector.get_books_genre()

    def test_get_books_for_children_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_new_book('LotR: Return of the Snake King')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        collector.set_book_genre('LotR: Return of the Snake King', 'Ужасы')
        assert collector.get_books_for_children()

    def test_add_book_in_favorites_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        assert 'LotR: Fellowship of the Python' in collector.favorites

    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        collector.delete_book_from_favorites('LotR: Fellowship of the Python')
        assert 'LotR: Fellowship of the Python' not in collector.favorites

    def test_get_list_of_favorites_books_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        assert 'LotR: Fellowship of the Python' in collector.get_list_of_favorites_books()
