from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from app.app_models import orderModels as om, bookModels as bm, employeeModels as em


class AccountViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        customer = om.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        book = om.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)
        order = om.Order.objects.create(customer_id=customer)
        order.goods.add(book)
        om.OrderInfo.objects.create(order_id=order, status='1', sale=10, order_price=100,
                                    delivery_date=datetime.now().date(), delivery_address='Test Address, street 1')
        em.Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', is_admin=True)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get('/lk/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    def test_get_redirect(self):
        response = self.client.get('/lk/')
        self.assertEquals(response.status_code, 302)

    def test_get_valid_by_name(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get(reverse('account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    def test_get_redirect_by_name(self):
        response = self.client.get(reverse('account'))
        self.assertEquals(response.status_code, 302)

    def test_get_customer(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.get(reverse('account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
        orders = response.context[0]['user']['orders']
        self.assertIsNotNone(orders)
        self.assertEquals(len(orders), 1)
        self.assertEquals(orders[0]['books'][0].title, 'Test Book')
        self.assertEquals(orders[0]['status'], '1')

    def test_get_employee(self):
        session = self.client.session
        session['role'] = 'adm'
        session['user'] = 'test@employee.com'
        session.save()
        response = self.client.get(reverse('account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')
        orders = response.context[0]['user'].get('orders')
        self.assertIsNone(orders)

    def test_post_redirect(self):
        response = self.client.post(reverse('account'))
        self.assertEquals(response.status_code, 302)

    def test_post_edit_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post(
            reverse('account'), data={'action': 'editMe'})
        self.assertEquals(response.status_code, 200)
        form = response.context[0]['form']
        self.assertIsNotNone(form)
        self.assertIsNotNone(form.fields)
        self.assertTemplateUsed(response, 'account.html')

    def test_post_save_valid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post(reverse('account'), data={'action': 'saveMe', 'name': 'New name',
                                                              'phone': '+375291111111', 'email': 'test@employee.com',
                                                              'password': 'testPassword1'})
        self.assertEquals(response.status_code, 302)

    def test_post_save_invalid(self):
        session = self.client.session
        session['role'] = 'usr'
        session['user'] = 'test@customer.com'
        session.save()
        response = self.client.post(reverse('account'), data={'action': 'saveMe', 'name': '',
                                                              'phone': '+375291111111', 'email': 'test@employee.com',
                                                              'password': 'testPassword1'})
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context[0]['form'].errors['name'], [
                          'This field is required.'])
        self.assertTemplateUsed(response, 'account.html')
