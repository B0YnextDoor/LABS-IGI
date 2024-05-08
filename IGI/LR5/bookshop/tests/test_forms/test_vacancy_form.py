from django.test import TestCase
from app.views.vacancyView import VacancyForm


class VacancyFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'name': 'Manager',
            'description': 'Text',
        }

    def test_form_labels(self):
        form = VacancyForm()
        self.assertEquals(form.fields['name'].label, 'Name')
        self.assertEquals(form.fields['description'].label, 'Description')

    def test_form_help_text(self):
        form = VacancyForm()
        self.assertEquals(form.fields['name'].help_text, 'Vacancy\'s name')
        self.assertEquals(
            form.fields['description'].help_text, 'Vacancy\'s description')

    def test_form_valid(self):
        form = VacancyForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['name'] = ''
        form = VacancyForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['name'], ['This field is required.'])
