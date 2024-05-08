from django.test import TestCase
from app.app_models import customerModel as cm, employeeModels as em
from app.repositories.authRepository import AuthRepository


class AuthRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.Customer.objects.create(name='Test Customer', phone='+375291111111',
                                   email='test@customer.com', password='testpassword')
        em.Employee.objects.create(name='Test Employee', phone='+375292222222',
                                   email='test@employee.com', password='testpassword', is_admin=True)

    def test_sign_up(self):
        new_customer = AuthRepository.sign_up(
            'New Customer', '+375293333333', 'new@customer.com', 'newpassword')
        self.assertIsNotNone(new_customer)
        self.assertEquals(new_customer.name, 'New Customer')
        self.assertEquals(new_customer.phone, '+375293333333')
        self.assertEquals(new_customer.email, 'new@customer.com')
        self.assertEquals(new_customer.password, 'newpassword')

    def test_sign_in_customer(self):
        user, role = AuthRepository.sign_in('test@customer.com')
        self.assertIsNotNone(user)
        self.assertEquals(role, 'usr')
        self.assertEquals(user.name, 'Test Customer')
        self.assertEquals(user.phone, '+375291111111')
        self.assertEquals(user.email, 'test@customer.com')
        self.assertEquals(user.password, 'testpassword')

    def test_sign_in_employee(self):
        user, role = AuthRepository.sign_in('test@employee.com')
        self.assertIsNotNone(user)
        self.assertEquals(role, 'emp')
        self.assertEquals(user.name, 'Test Employee')
        self.assertEquals(user.phone, '+375292222222')
        self.assertEquals(user.email, 'test@employee.com')
        self.assertEquals(user.password, 'testpassword')
