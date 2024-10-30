from django.test import TestCase
from django.urls import reverse
from datetime import datetime, timedelta
from app.app_models import orderModels as om, bookModels as bm


class OrderViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        customer = om.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='Testpassword1')
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        book = om.Book.objects.create(
            title='Test Book', price=110.0, amount=10, genre=genre, author=author)
        order = om.Order.objects.create(customer_id=customer)
        order.goods.add(book)
        om.OrderInfo.objects.create(order_id=order, status='0', sale=10, order_price=100,
                                    delivery_date=datetime.now() + timedelta(days=1),
                                    delivery_address='Minsk, M.Bogdanovicha 29')
        cls.form_data = {
            'books': [],
            'date': datetime.now().date() + timedelta(days=2),
            'address': 'Minsk, Test street 1',
            'sale_code': ''
        }

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get('/orders/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('order.html')
        self.assertIsNotNone(response.context[0]['orders'])

    def test_get_invalid(self):
        response = self.client.get('/orders/')
        self.assertEquals(response.status_code, 302)

    def test_get_by_name(self):
        session = self.client.session
        session['role'] = 'adm'
        session.save()
        response = self.client.get(reverse('order'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('order.html')
        self.assertIsNotNone(response.context[0]['orders'])

    def test_post_invalid(self):
        session = self.client.session
        session['role'] = 'adm'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post('/orders/')
        self.assertEquals(response.status_code, 302)

    def test_post_buy(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post('/orders/', {'action': 'buy'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order.html')
        self.assertIsNone(response.context[0]['orders'])
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_create_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        self.form_data['action'] = 'create'
        response = self.client.post('/orders/', data=self.form_data)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order.html')
        self.assertIsNotNone(response.context[0]['form'])
        self.assertEquals(
            response.context[0]['form'].errors['books'], ['Choose at least 1 book'])


class OrderDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        customer = om.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='Testpassword1')
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        book = om.Book.objects.create(
            title='Test Book', price=110.0, amount=10, genre=genre, author=author)
        order = om.Order.objects.create(customer_id=customer)
        order.goods.add(book)
        om.OrderInfo.objects.create(order_id=order, status='0', sale=10, order_price=100,
                                    delivery_date=datetime.now() + timedelta(days=1),
                                    delivery_address='Minsk, M.Bogdanovicha 29')

    def test_get_invalid(self):
        response = self.client.get('/orders/1')
        self.assertEquals(response.status_code, 302)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get('/orders/1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order-detail.html')
        self.assertIsNotNone(response.context[0]['order'])

    def test_post_invalid(self):
        response = self.client.post('/orders/1')
        self.assertEquals(response.status_code, 302)

    def test_post_edit(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post('/orders/1', {'action': 'edit'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order-detail.html')
        self.assertIsNotNone(response.context[0]['form'])

    def test_post_del(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post('/orders/1', {'action': 'del'})
        self.assertEquals(response.status_code, 302)

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post('/orders/1', {'action': 'save', 'books': [],
                                                  'date': datetime.now().date() + timedelta(days=2),
                                                  'address': 'Minsk, Test street 2',
                                                  'sale_code': ''})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order-detail.html')
        self.assertIsNotNone(response.context[0]['form'])
