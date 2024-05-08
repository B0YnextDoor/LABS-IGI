from django.test import TestCase
from app.app_models import bookModels as bm


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        bm.Author.objects.create(name='John', surname='Doe')

    def test_name_label(self):
        author = bm.Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_surname_label(self):
        author = bm.Author.objects.get(id=1)
        field_label = author._meta.get_field('surname').verbose_name
        self.assertEquals(field_label, 'surname')

    def test_object_name_is_surname_comma_name(self):
        author = bm.Author.objects.get(id=1)
        expected_object_name = f'{author.id} {author.surname} {author.name} {author.created_at} {author.updated_at}'
        self.assertEquals(expected_object_name, str(author))


class BookGenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        bm.BookGenre.objects.create(name='Fiction')

    def test_name_label(self):
        genre = bm.BookGenre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_object_name_is_name(self):
        genre = bm.BookGenre.objects.get(id=1)
        expected_object_name = f'{genre.id} {genre.name} {genre.created_at} {genre.updated_at}'
        self.assertEquals(expected_object_name, str(genre))


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        bm.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)

    def test_title_label(self):
        book = bm.Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_price_label(self):
        book = bm.Book.objects.get(id=1)
        field_label = book._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_amount_label(self):
        book = bm.Book.objects.get(id=1)
        field_label = book._meta.get_field('amount').verbose_name
        self.assertEquals(field_label, 'amount')

    def test_genre_label(self):
        book = bm.Book.objects.get(id=1)
        field_label = book._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_author_label(self):
        book = bm.Book.objects.get(id=1)
        field_label = book._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')

    def test_get_absolute_url(self):
        book = bm.Book.objects.get(id=1)
        abs_url = book.get_absolute_url()
        self.assertEquals(abs_url, '/books/1')

    def test_object_name_is_title_author_genre_price_amount(self):
        book = bm.Book.objects.get(id=1)
        expected_object_name = f'{book.id} {book.title} {book.author} {book.genre} {book.price} {book.amount} {book.created_at} {book.updated_at}'
        self.assertEquals(expected_object_name, str(book))
