from django.test import TestCase
from datetime import datetime, timedelta
from app.app_models import orderModels as om, bookModels as bm
from app.services.orderService import OrderService


class OrderServiceTest(TestCase):
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
        om.OrderInfo.objects.create(order_id=order, status='0', sale=10, delivery_date=datetime.now(
        ), delivery_address='Test Address', order_price=100)

    def test_get_all(self):
        orders = OrderService.get_all()
        self.assertIsNotNone(orders)
        self.assertEquals(len(orders), 1)
        self.assertEquals(orders[0]['id'], 1)
        self.assertEquals(orders[0]['customer']['name'], 'Test Customer')
        self.assertEquals(orders[0]['status'], '1')
        self.assertEquals(orders[0]['price'], 100)

    def test_get_user_orders(self):
        user = om.Customer.objects.get(id=1)
        orders = OrderService.get_user_orders(user)
        self.assertIsNotNone(orders)
        self.assertEquals(len(orders), 1)
        self.assertEquals(orders[0]['id'], 1)
        self.assertEquals(orders[0]['status'], '1')

    def test_get_by_id(self):
        order = OrderService.get_by_id(1)
        self.assertIsNotNone(order)
        self.assertEquals(order['status'], '0')

    def test_create_order(self):
        new_odrer = OrderService.create_order(
            'test@customer.com', ['1'], datetime.now(), 'Aboba street', 0.1)
        self.assertIsNotNone(new_odrer)
        self.assertEquals(new_odrer.orderinfo.status, '0')
        self.assertEquals(new_odrer.orderinfo.order_price, 17.991)

    def test_update_order(self):
        order = OrderService.update_order(
            1, ['1'], datetime.now() + timedelta(days=1), 'Aboba street', 0)
        self.assertIsNotNone(order)
        self.assertEquals(order.orderinfo.order_price, 19.99)
        self.assertEquals(order.orderinfo.delivery_date.date(),
                          (datetime.now() + timedelta(days=1)).date())

    def test_cancel_order(self):
        order = OrderService.cancel_order(1)
        self.assertEquals(order, 'ok')
