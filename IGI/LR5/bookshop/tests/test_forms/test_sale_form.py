from django.test import TestCase
from app.views.saleView import SaleCodeForm


class SaleCodeFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'code': 'code_10',
            'is_active': False,
        }

    def test_form_labels(self):
        form = SaleCodeForm()
        self.assertEquals(form.fields['code'].label, 'Code')
        self.assertEquals(form.fields['is_active'].label, 'Is active')

    def test_form_help_text(self):
        form = SaleCodeForm()
        self.assertEquals(form.fields['code'].help_text, 'Sale code')
        self.assertEquals(form.fields['is_active'].help_text, 'Is code active')

    def test_form_valid(self):
        form = SaleCodeForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)

    def test_form_invalid(self):
        self.form_data['code'] = ''
        form = SaleCodeForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['code'], ['This field is required.'])

    def test_form_invalid_code(self):
        self.form_data['code'] = 'code123'
        form = SaleCodeForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[
                          0], 'Sale code must match `code-part`_`sale-part`')
