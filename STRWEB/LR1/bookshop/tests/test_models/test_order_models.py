from django.test import TestCase
from datetime import datetime
from app.app_models import orderModels as om, bookModels as bm


class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        customer = om.Customer.objects.create(
            name='Test Customer', phone='+375291111111', email='test@customer.com', password='testpassword')
        genre = bm.BookGenre.objects.create(name='Fiction')
        author = bm.Author.objects.create(name='John', surname='Doe')
        book = om.Book.objects.create(
            title='Test Book', price=19.99, amount=10, genre=genre, author=author)
        order = om.Order.objects.create(customer_id=customer)
        order.goods.add(book)

    def test_customer_id_label(self):
        order = om.Order.objects.get(id=1)
        field_label = order._meta.get_field('customer_id').verbose_name
        self.assertEquals(field_label, 'customer id')

    def test_goods_label(self):
        order = om.Order.objects.get(id=1)
        field_label = order._meta.get_field('goods').verbose_name
        self.assertEquals(field_label, 'goods')

    def test_object_name_is_customer_id(self):
        order = om.Order.objects.get(id=1)
        expected_object_name = f'{order.id} {order.customer_id} {order.created_at} {order.updated_at}'
        self.assertEquals(expected_object_name, str(order))


class OrderInfoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
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

    def test_order_id_label(self):
        order_info = om.OrderInfo.objects.get(id=1)
        field_label = order_info._meta.get_field('order_id').verbose_name
        self.assertEquals(field_label, 'order id')

    def test_status_label(self):
        order_info = om.OrderInfo.objects.get(id=1)
        field_label = order_info._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_sale_label(self):
        order_info = om.OrderInfo.objects.get(id=1)
        field_label = order_info._meta.get_field('sale').verbose_name
        self.assertEquals(field_label, 'sale')

    def test_delivery_date_label(self):
        order_info = om.OrderInfo.objects.get(id=1)
        field_label = order_info._meta.get_field('delivery_date').verbose_name
        self.assertEquals(field_label, 'delivery date')

    def test_delivery_address_label(self):
        order_info = om.OrderInfo.objects.get(id=1)
        field_label = order_info._meta.get_field(
            'delivery_address').verbose_name
        self.assertEquals(field_label, 'delivery address')

    def test_order_price_label(self):
        order_info = om.OrderInfo.objects.get(id=1)
        field_label = order_info._meta.get_field('order_price').verbose_name
        self.assertEquals(field_label, 'order price')

    def test_status_max_length(self):
        order_info = om.OrderInfo.objects.get(id=1)
        max_length = order_info._meta.get_field('status').max_length
        self.assertEquals(max_length, 1)

    def test_object_name_is_order_id_delivery_date_delivery_address_order_price_status_sale(self):
        order_info = om.OrderInfo.objects.get(id=1)
        expected_object_name = f'{order_info.id} {order_info.order_id} {order_info.delivery_date} {order_info.delivery_address} {order_info.order_price} {order_info.status} {order_info.sale} {order_info.created_at} {order_info.updated_at}'
        self.assertEquals(expected_object_name, str(order_info))
