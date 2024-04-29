from main import BooksCollector
import pytest


class TestBooksCollector:


    @pytest.mark.parametrize('name', ['LotR: Fellowship of the Pyhton and how they miss Boromir', ''])
    def test_add_new_book_add_book_negative_cases(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_not_found_genre(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика1')
        assert collector.get_book_genre('LotR: Fellowship of the Python') == ''

    def test_set_book_genre_replace_genre_correct(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Ужасы')
        assert collector.get_book_genre('LotR: Fellowship of the Python') == 'Ужасы'

    def test_get_books_with_specific_genre_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        collector.add_new_book('LotR: Return of the Snake King')
        collector.set_book_genre('LotR: Return of the Snake King', 'Ужасы')
        collector.add_new_book('LotR: Return of the Python King')
        collector.set_book_genre('LotR: Return of the Python King', 'Ужасы')
        assert ['LotR: Return of the Snake King', 'LotR: Return of the Python King'] == collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_genre_no_duple_check(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_new_book('LotR: Fellowship of the Python')
        assert collector.get_books_genre() == {'LotR: Fellowship of the Python' : ''}

    def test_get_books_for_children_check_correct_method_work(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_new_book('LotR: Return of the Snake King')
        collector.set_book_genre('LotR: Fellowship of the Python', 'Фантастика')
        collector.set_book_genre('LotR: Return of the Snake King', 'Ужасы')
        assert collector.get_books_for_children() == ['LotR: Fellowship of the Python']

    def test_add_book_in_favorites_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        assert collector.get_list_of_favorites_books() == ['LotR: Fellowship of the Python']

    def test_delete_book_from_favorites_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        collector.delete_book_from_favorites('LotR: Fellowship of the Python')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_no_duple_check(self):
        collector = BooksCollector()
        collector.add_new_book('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        collector.add_book_in_favorites('LotR: Fellowship of the Python')
        assert collector.get_list_of_favorites_books() == ['LotR: Fellowship of the Python']
