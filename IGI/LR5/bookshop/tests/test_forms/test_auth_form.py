from django.test import TestCase
from app.views.authView import SignInForm, SignUpForm


class SignUpFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'name': 'Test User',
            'phone': '+375291111111',
            'email': 'test@test.com',
            'password': 'test123Test',
            'confirmation': True,
        }

    def test_form_labels(self):
        form = SignUpForm()
        self.assertEquals(form.fields['name'].label, 'Name')
        self.assertEquals(form.fields['phone'].label, 'Phone')
        self.assertEquals(form.fields['email'].label, 'Email')
        self.assertEquals(form.fields['password'].label, 'Password')
        self.assertEquals(form.fields['confirmation'].label, None)

    def test_form_help_text(self):
        form = SignUpForm()
        self.assertEquals(form.fields['name'].help_text, 'Name')
        self.assertEquals(form.fields['phone'].help_text, 'Phone number')
        self.assertEquals(form.fields['email'].help_text, 'Email')
        self.assertEquals(form.fields['password'].help_text, 'Password')
        self.assertEquals(
            form.fields['confirmation'].help_text, 'I confirm that I am over 18 years old.')

    def test_form_valid(self):
        form = SignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['confirmation'] = False
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['confirmation'], [
                          'This field is required.'])

    def test_form_phone_invalid(self):
        self.form_data['phone'] = '1234567890'
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(
            form.non_field_errors()[0], 'Phone number must matches `+37529xxxxxxx`!')

    def test_form_password_invalid(self):
        self.form_data['password'] = '12345678'
        form = SignUpForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.non_field_errors()[0],
                          'Password must contain at least 1 capital letter!')

    def test_clean(self):
        form = SignUpForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.cleaned_data, self.form_data)


class SignInFormTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.form_data = {
            'email': 'test@test.com',
            'password': 'test123Test',
        }

    def test_form_labels(self):
        form = SignInForm()
        self.assertEquals(form.fields['email'].label, 'Email')
        self.assertEquals(form.fields['password'].label, 'Password')

    def test_form_hel_text(self):
        form = SignInForm()
        self.assertEquals(form.fields['email'].help_text, 'Email')
        self.assertEquals(form.fields['password'].help_text, 'Password')

    def test_form_valid(self):
        form = SignInForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        self.form_data['password'] = ''
        form = SignInForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password'], [
                          'This field is required.'])
