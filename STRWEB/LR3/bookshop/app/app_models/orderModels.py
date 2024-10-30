from app.app_models.baseModel import models, BaseModel
from app.app_models.customerModel import Customer
from app.app_models.bookModels import Book
from django.urls import reverse


class Order(BaseModel):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    goods = models.ManyToManyField(
        Book, through='OrderItem', related_name='orders', help_text='Goods list')

    class Meta:
        db_table = 'orders_table'
        ordering = ['customer_id']

    def get_absolute_url(self):
        """
        Returns the url to access a particular order instance.
        """
        return reverse('order-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return f'{self.id} {self.customer_id} {self.created_at} {self.updated_at}'


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1, help_text='Quantity of books in the order')

    class Meta:
        db_table = 'order_items_table'
        unique_together = ('order', 'book')

    def __str__(self):
        return f'Order {self.order.id}: {self.book.title} - {self.quantity}'


class OrderInfo(BaseModel):
    order_id = models.OneToOneField(
        Order, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=1, default='0', help_text='Order\'s status')
    sale = models.PositiveSmallIntegerField(
        default=0, help_text='Order\'s sale')
    delivery_date = models.DateTimeField(help_text='Delivery date & time')
    delivery_address = models.TextField(
        help_text='Delivery address', default='Minsk, ')
    order_price = models.FloatField(help_text='Order\'s price')

    class Meta:
        db_table = 'orders_info_table'
        ordering = ['delivery_date']

    def __str__(self) -> str:
        return f'{self.id} {self.order_id} {self.delivery_date} {self.delivery_address} {self.order_price} {self.status} {self.sale} {self.created_at} {self.updated_at}'
