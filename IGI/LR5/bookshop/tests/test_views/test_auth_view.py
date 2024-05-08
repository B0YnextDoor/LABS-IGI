from django.test import TestCase
from django.urls import reverse
from app.app_models import customerModel as cm


class SignUpViewTest(TestCase):
    def test_get(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.get('/sign-up/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth.html')

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.get(reverse('signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth.html')

    def test_post_valid(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.post(reverse('signup'), {'name': 'Test customer', 'phone': '+375291111111',
                                                        'email': 'test@customer.com', 'password': 'Testpassword1',
                                                        'confirmation': True})
        self.assertEquals(response.status_code, 302)

    def test_post_invalid_phone(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.post(reverse('signup'), {'name': 'Test customer', 'phone': '1111111111111',
                                                        'email': 'test@customer.com', 'password': 'Testpassword1',
                                                        'confirmation': True})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context[0]['form'].non_field_errors()[0], 'Phone number must matches `+37529xxxxxxx`!')

    def test_post_invalid_password(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.post(reverse('signup'), {'name': 'Test customer', 'phone': '+375291234567',
                                                        'email': 'test@customer.com', 'password': 'testpassword1',
                                                        'confirmation': True})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context[0]['form'].non_field_errors()[0], 'Password must contain at least 1 capital letter!')

    def test_post_invalid_confirmation(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.post(reverse('signup'), {'name': 'Test customer', 'phone': '+375291234567',
                                                        'email': 'test@customer.com', 'password': 'Testpassword1'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(
            response.context[0]['form'].errors['confirmation'], ['This field is required.'])


class SignInViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cm.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='Testpassword1')

    def test_get(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.get('/sign-in/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth.html')

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.get(reverse('signin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth.html')

    def test_post_valid(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.post(
            reverse('signin'), {'email': 'test@customer.com', 'password': 'Testpassword1'})
        self.assertEquals(response.status_code, 302)

    def test_post_invalid_credentials(self):
        session = self.client.session
        session['role'] = ''
        session.save()
        response = self.client.post(
            reverse('signin'), {'email': 'test@customer.com', 'password': 'testpassword1'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context[0]['form'].non_field_errors()[
                          0], 'Wrong email or password!')


class LogOutViewTest(TestCase):
    def test_get(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.get('/log-out/')
        self.assertEquals(response.status_code, 302)

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = 'usr'
        session.save()
        response = self.client.get(reverse('log-out'))
        self.assertEquals(response.status_code, 302)
