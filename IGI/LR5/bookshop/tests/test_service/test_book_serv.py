from django.test import TestCase
from app.app_models import bookModels as bm
from app.services.bookService import BookService


class BookServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        bm.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)

    def test_get_all(self):
        books = BookService.get_all('amount')
        self.assertIsNotNone(books)
        self.assertEquals(len(books), 1)
        self.assertEquals(books[0].title, 'Test Book')

    def test_get_by_id(self):
        book = BookService.get_by_id(1)
        self.assertIsNotNone(book)
        self.assertEquals(book.title, 'Test Book')

    def test_create(self):
        genre = bm.BookGenre.objects.get(id=1)
        author = bm.Author.objects.get(id=1)
        new_book = BookService.create(
            'New Book', 9.99, 5, genre.id, author.id)
        self.assertIsNotNone(new_book)
        self.assertEquals(new_book.title, 'New Book')
        self.assertEquals(new_book.price, 9.99)
        self.assertEquals(new_book.amount, 5)
        self.assertEquals(new_book.genre, genre)
        self.assertEquals(new_book.author, author)

    def test_update(self):
        genre = bm.BookGenre.objects.get(id=1)
        author = bm.Author.objects.get(id=1)
        updated_book = BookService.update(
            1, 'Updated Book', 4.99, 3, genre.id, author.id)
        self.assertIsNotNone(updated_book)
        self.assertEquals(updated_book.title, 'Updated Book')
        self.assertEquals(updated_book.price, 4.99)
        self.assertEquals(updated_book.amount, 3)
        self.assertEquals(updated_book.genre, genre)
        self.assertEquals(updated_book.author, author)

    def test_delete(self):
        BookService.delete(1)
        deleted_book = BookService.get_by_id(1)
        self.assertIsNone(deleted_book)
