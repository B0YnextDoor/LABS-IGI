from django.test import TestCase
from app.views.qaView import QAForm


class QAFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'question': 'WUT?',
            'answer': 'YES',
        }

    def test_form_labels(self):
        form = QAForm()
        self.assertEquals(form.fields['question'].label, 'Question')
        self.assertEquals(form.fields['answer'].label, 'Answer')

    def test_form_help_text(self):
        form = QAForm()
        self.assertEquals(form.fields['question'].help_text, 'Question')
        self.assertEquals(form.fields['answer'].help_text, 'Answer')

    def test_form_valid(self):
        form = QAForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['answer'] = ''
        form = QAForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['answer'], ['This field is required.'])
