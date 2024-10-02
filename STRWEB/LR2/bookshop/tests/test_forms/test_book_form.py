from django.test import TestCase
from app.views.bookView import BookDetailForm
from app.app_models import bookModels as bm


class BookFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        cls.form_data = {
            'title': 'Test',
            'price': 123.123,
            'amount': 5,
            'genre': genre,
            'author': author
        }

    def test_form_labels(self):
        form = BookDetailForm()
        self.assertEquals(form.fields['title'].label, 'Title')
        self.assertEquals(form.fields['price'].label, 'Price')
        self.assertEquals(form.fields['amount'].label, 'Amount')
        self.assertEquals(form.fields['genre'].label, 'Genre')
        self.assertEquals(form.fields['author'].label, 'Author')

    def test_form_help_text(self):
        form = BookDetailForm()
        self.assertEquals(form.fields['title'].help_text, 'Book\'s title')
        self.assertEquals(form.fields['price'].help_text, 'Book\'s price')
        self.assertEquals(
            form.fields['amount'].help_text, 'Amount of copies in the shop')
        self.assertEquals(form.fields['genre'].help_text, '')
        self.assertEquals(form.fields['author'].help_text, '')

    def test_form_valid(self):
        form = BookDetailForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['title'] = ''
        form = BookDetailForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['title'], ['This field is required.'])

    def test_form_price_invalid(self):
        self.form_data['price'] = -10
        form = BookDetailForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.non_field_errors()[0], 'Wrong price format')

    def test_clean(self):
        form = BookDetailForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)
