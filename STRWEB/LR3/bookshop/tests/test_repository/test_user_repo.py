from django.test import TestCase
from app.app_models import customerModel as cm
from app.repositories.userRepository import UserRepository


class UserRepositoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = cm.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')
        cm.CustomerReview.objects.create(
            user=user, rate=5, text='This is a test review')

    def test_get_by_email(self):
        user = UserRepository.get_by_email('test@customer.com')
        self.assertIsNotNone(user)
        self.assertEquals(user.id, 1)
        self.assertEquals(user.name, 'Test Customer')
        self.assertEquals(user.phone, '+375291111111')
        self.assertEquals(user.email, 'test@customer.com')
        self.assertEquals(user.password, 'testpassword')

    def test_update(self):
        user = UserRepository.update(
            'test@customer.com', 'Man', '+375291111111', 'test1@test.com', 'testtesttest')
        self.assertIsNotNone(user)
        self.assertEquals(user.id, 1)
        self.assertEquals(user.name, 'Man')
        self.assertEquals(user.phone, '+375291111111')
        self.assertEquals(user.email, 'test1@test.com')
        self.assertEquals(user.password, 'testtesttest')

    def test_get_reviews(self):
        rews = UserRepository.get_reviews()
        self.assertIsNotNone(rews)
        self.assertEquals(len(rews), 1)
        self.assertEquals(rews[0].id, 1)
        self.assertEquals(rews[0].user.id, 1)
        self.assertEquals(rews[0].rate, 5)
        self.assertEquals(rews[0].text, 'This is a test review')

    def test_get_review_by_id(self):
        rew = UserRepository.get_review_by_id(1)
        self.assertIsNotNone(rew)
        self.assertEquals(rew.id, 1)
        self.assertEquals(rew.user.id, 1)
        self.assertEquals(rew.rate, 5)
        self.assertEquals(rew.text, 'This is a test review')

    def test_create_review(self):
        rew = UserRepository.create_review('test@customer.com', 4, 'Aboba')
        self.assertIsNotNone(rew)
        self.assertEquals(rew.user.id, 1)
        self.assertEquals(rew.rate, 4)
        self.assertEquals(rew.text, 'Aboba')

    def test_update_review(self):
        rew = UserRepository.update_review(1, 5, 'Upd text')
        self.assertIsNotNone(rew)
        self.assertEquals(rew.user.id, 1)
        self.assertEquals(rew.rate, 5)
        self.assertEquals(rew.text, 'Upd text')

    def test_delete_review(self):
        rew = UserRepository.delete_review(1)
        self.assertEquals(rew, 'ok')
