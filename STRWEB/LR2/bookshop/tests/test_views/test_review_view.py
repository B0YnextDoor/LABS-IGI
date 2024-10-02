from django.test import TestCase
from django.urls import reverse
from app.app_models.customerModel import Customer, CustomerReview


class ReviewViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        user1 = Customer.objects.create(
            name='Test Customer1', phone='+375291111111', email='test1@customer.com', password='Testpassword1')
        user2 = Customer.objects.create(
            name='Test Customer2', phone='+375292222222', email='test2@customer.com', password='Testpassword1')
        CustomerReview.objects.create(
            user=user1, rate=5, text='This is a test review')
        CustomerReview.objects.create(user=user2, rate=3, text='Text')

    def test_get(self):
        response = self.client.get('/reviews/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        reviews = response.context[0]['reviews']
        self.assertIsNotNone(reviews)
        self.assertEquals(len(reviews), 2)

    def test_get_by_name(self):
        response = self.client.get(reverse('reviews'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        reviews = response.context[0]['reviews']
        self.assertIsNotNone(reviews)
        self.assertEquals(len(reviews), 2)

    def test_post_with_no_role(self):
        response = self.client.post(reverse('reviews'))
        self.assertEquals(response.status_code, 302)

    def test_post_invalid(self):
        session = self.client.session
        session['role'] = 'emp'
        session.save()
        response = self.client.post(reverse('reviews'), {'action': 'add'})
        self.assertEquals(response.status_code, 302)

    def test_post_add(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test1@customer.com'
        session.save()
        response = self.client.post(reverse('reviews'), {'action': 'add'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['action'], 'add')
        self.assertEquals(response.context[0]['email'], 'test1@customer.com')

    def test_post_del_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test1@customer.com'
        session.save()
        response = self.client.post(reverse('reviews'), {'action': 'del_1'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomerReview.objects.count(), 1)
        self.assertIsNone(CustomerReview.objects.filter(id=1).first())

    def test_post_del_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test3@customer.com'
        session.save()
        response = self.client.post(reverse('reviews'), {'action': 'del_1'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomerReview.objects.count(), 2)
        self.assertIsNotNone(CustomerReview.objects.filter(id=1).first())

    def test_post_upd_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test1@customer.com'
        session.save()
        response = self.client.post(reverse('reviews'), {'action': 'upd_1'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['action'], 1)

    def test_post_upd_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test3@customer.com'
        session.save()
        response = self.client.post(reverse('reviews'), {'action': 'upd_1'})
        self.assertEquals(response.status_code, 302)

    def test_post_save_add_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test1@customer.com'
        session.save()
        response = self.client.post(
            reverse('reviews'), {'action': 'save_add', 'rate': 5, 'text': 'New rev'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomerReview.objects.count(), 3)
        self.assertIsNotNone(CustomerReview.objects.filter(id=3).first())
        self.assertEquals(CustomerReview.objects.get(id=3).text, 'New rev')

    def test_post_save_add_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test1@customer.com'
        session.save()
        response = self.client.post(
            reverse('reviews'), {'action': 'save_add', 'rate': 15, 'text': 'New rev'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].non_field_errors()[
                          0], 'Rate must be an integer number in range 0-5')
        self.assertEquals(CustomerReview.objects.count(), 2)

    def test_post_save_upd_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test2@customer.com'
        session.save()
        response = self.client.post(
            reverse('reviews'), {'action': 'save_2', 'rate': 5,
                                 'text': f'P.S. Rev updated.'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(CustomerReview.objects.count(), 2)
        self.assertEquals(CustomerReview.objects.get(id=2).rate, 5)

    def test_post_save_upd_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test2@customer.com'
        session.save()
        response = self.client.post(
            reverse('reviews'), {'action': 'save_2', 'rate': 5, 'text': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'review.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(response.context[0]['form'].errors['text'], [
                          'This field is required.'])
