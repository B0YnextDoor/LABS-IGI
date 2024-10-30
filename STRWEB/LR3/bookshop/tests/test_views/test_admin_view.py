from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from app.app_models import bookModels as bm, employeeModels as em, orderModels as om


class AdminViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        customer = om.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        book = om.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)
        order = om.Order.objects.create(customer_id=customer)
        order.goods.add(book)
        om.OrderInfo.objects.create(order_id=order, status='1', sale=10, delivery_date=datetime.now(
        ), delivery_address='Minsk, M. Bogdanovicha 29', order_price=100)
        em.Employee.objects.create(
            name='Test Employee', phone='+375291111111', email='test@employee.com', password='testpassword', is_admin=True)

    def test_get_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session['user'] = 'test@employee.com'
        session.save()
        response = self.client.get('/admin-pannel/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin.html')

    def test_get_by_name_valid(self):
        session = self.client.session
        session['role'] = 'adm'
        session['user'] = 'test@employee.com'
        session.save()
        response = self.client.get(reverse('admin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin.html')

    def test_get_invalid(self):
        session = self.client.session
        session['role'] = 'emp'
        session['user'] = 'test@employee.com'
        session.save()
        response = self.client.get(reverse('admin'))
        self.assertEquals(response.status_code, 302)
