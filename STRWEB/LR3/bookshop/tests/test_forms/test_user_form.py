from django.test import TestCase
from app.views.accountView import UserForm


class UserFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'name': 'Test User',
            'phone': '+375291111111',
            'email': 'test@test.com',
            'password': 'test123Test'
        }

    def test_form_labels(self):
        form = UserForm()
        self.assertEquals(form.fields['name'].label, 'Name')
        self.assertEquals(form.fields['phone'].label, 'Phone')
        self.assertEquals(form.fields['email'].label, 'Email')
        self.assertEquals(form.fields['password'].label, 'Password')

    def test_form_help_text(self):
        form = UserForm()
        self.assertEquals(form.fields['name'].help_text, 'Name')
        self.assertEquals(form.fields['phone'].help_text, 'Phone number')
        self.assertEquals(form.fields['email'].help_text, 'Email')
        self.assertEquals(form.fields['password'].help_text, 'Password')

    def test_form_valid(self):
        form = UserForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['name'] = ''
        form = UserForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['name'], ['This field is required.'])

    def test_form_phone_invalid(self):
        self.form_data['phone'] = '1234567890'
        form = UserForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.non_field_errors()[0], 'Phone number must matches `+37529xxxxxxx`!')

    def test_form_password_invalid(self):
        self.form_data['password'] = 'abcdEfg'
        form = UserForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[
                          0], 'Password min length is 8!')
        self.assertEquals(form.non_field_errors()[1],
                          'Password must contain at least 1 digit!')

    def test_clean(self):
        form = UserForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)
