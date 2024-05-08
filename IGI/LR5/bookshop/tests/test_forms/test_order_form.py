from django.test import TestCase
from datetime import datetime, timedelta
from app.views.orderView import OrderForm
from app.app_models.bookModels import Book, Author, BookGenre


class OrderFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        genre = BookGenre.objects.create(name='Fiction')
        author = Author.objects.create(name='John', surname='Doe')
        book = Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)
        cls.form_data = {
            'books': [str(book.id)],
            'date': datetime.now().date() + timedelta(days=1),
            'address': 'Minsk, M. Bogdanovich 29',
            'sale_code': ''
        }

    def test_form_labels(self):
        form = OrderForm()
        self.assertEquals(form.fields['books'].label, None)
        self.assertEquals(form.fields['date'].label, None)
        self.assertEquals(form.fields['address'].label, None)
        self.assertEquals(form.fields['sale_code'].label, None)

    def test_form_help_text(self):
        form = OrderForm()
        self.assertEquals(form.fields['books'].help_text, '')
        self.assertEquals(form.fields['date'].help_text, '')
        self.assertEquals(form.fields['address'].help_text,
                          'Enter a delivery address(pickup address as default)')
        self.assertEquals(form.fields['sale_code'].help_text, '')

    def test_form_valid(self):
        form = OrderForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid_date(self):
        self.form_data['date'] = datetime.now().date()
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[
                          0], 'The date cannot be in the past!')

    def test_form_invalid_books(self):
        self.form_data['books'] = list()
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        print(form.errors)
        self.assertEquals(form.errors['books'], ['Choose at least 1 book'])

    def test_form_invalid_address(self):
        self.form_data['address'] = 'Minsk, 1213'
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[
                          0], 'Address must match: `city`,`street`')

    def test_form_invalid_sale_code(self):
        self.form_data['sale_code'] = 'aboba'
        form = OrderForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[
                          0], 'Sale code doesn\'t exist')
