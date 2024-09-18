from django.test import TestCase
from app.views.infoView import InfoForm


class InfoFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'info': 'Test info'
        }

    def test_form_labels(self):
        form = InfoForm()
        self.assertEquals(form.fields['info'].label, 'Info')

    def test_form_help_text(self):
        form = InfoForm()
        self.assertEquals(form.fields['info'].help_text, 'Company\'s info')

    def test_form_valid(self):
        form = InfoForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['info'] = ''
        form = InfoForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['info'], ['This field is required.'])
