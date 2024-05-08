from django.test import TestCase
from app.views.reviewView import ReviewForm


class ReviewFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'rate': 3,
            'text': 'text',
        }

    def test_form_labels(self):
        form = ReviewForm()
        self.assertEquals(form.fields['rate'].label, 'Rate')
        self.assertEquals(form.fields['text'].label, 'Text')

    def test_form_help_text(self):
        form = ReviewForm()
        self.assertEquals(form.fields['rate'].help_text, 'Rate (0-5)')
        self.assertEquals(form.fields['text'].help_text, 'Review\'s text')

    def test_form_valid(self):
        form = ReviewForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['text'] = ''
        form = ReviewForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['text'], ['This field is required.'])

    def test_form_invalid_rate(self):
        self.form_data['rate'] = 10
        form = ReviewForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[
                          0], 'Rate must be an integer number in range 0-5')
