from django.test import TestCase
from app.app_models import customerModel as cm


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cm.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')

    def test_name_label(self):
        customer = cm.Customer.objects.get(id=1)
        field_label = customer._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_phone_label(self):
        customer = cm.Customer.objects.get(id=1)
        field_label = customer._meta.get_field('phone').verbose_name
        self.assertEquals(field_label, 'phone')

    def test_email_label(self):
        customer = cm.Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        customer = cm.Customer.objects.get(id=1)
        field_label = customer._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')

    def test_name_max_length(self):
        customer = cm.Customer.objects.get(id=1)
        max_length = customer._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_phone_max_length(self):
        customer = cm.Customer.objects.get(id=1)
        max_length = customer._meta.get_field('phone').max_length
        self.assertEquals(max_length, 13)

    def test_password_max_length(self):
        customer = cm.Customer.objects.get(id=1)
        max_length = customer._meta.get_field('password').max_length
        self.assertEquals(max_length, 300)

    def test_object_name_is_name_phone_email_password(self):
        customer = cm.Customer.objects.get(id=1)
        expected_object_name = f'{customer.id} {customer.name} {customer.phone} {customer.email} {customer.password} {customer.created_at} {customer.updated_at}'
        self.assertEquals(expected_object_name, str(customer))


class CustomerReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = cm.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')
        cm.CustomerReview.objects.create(
            user=user, rate=5, text='This is a test review')

    def test_user_label(self):
        review = cm.CustomerReview.objects.get(id=1)
        field_label = review._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_rate_label(self):
        review = cm.CustomerReview.objects.get(id=1)
        field_label = review._meta.get_field('rate').verbose_name
        self.assertEquals(field_label, 'rate')

    def test_text_label(self):
        review = cm.CustomerReview.objects.get(id=1)
        field_label = review._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_object_name_is_user_rate_text(self):
        review = cm.CustomerReview.objects.get(id=1)
        expected_object_name = f'{review.id} {review.user.name} {review.rate} {review.text} {review.created_at} {review.updated_at}'
        self.assertEquals(expected_object_name, str(review))
