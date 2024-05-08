from django.test import TestCase
from app.views.newsView import NewsForm


class NewsFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'title': 'Test',
            'text': 'Test.',
            'img': None
        }

    def test_form_labels(self):
        form = NewsForm()
        self.assertEquals(form.fields['title'].label, 'Title')
        self.assertEquals(form.fields['text'].label, 'Text')
        self.assertEquals(form.fields['img'].label, 'Img')

    def test_form_help_text(self):
        form = NewsForm()
        self.assertEquals(form.fields['title'].help_text, 'News title')
        self.assertEquals(form.fields['text'].help_text, 'News summary')
        self.assertEquals(form.fields['img'].help_text, 'News photo')

    def test_form_valid(self):
        form = NewsForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['title'] = ''
        form = NewsForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['title'], ['This field is required.'])
