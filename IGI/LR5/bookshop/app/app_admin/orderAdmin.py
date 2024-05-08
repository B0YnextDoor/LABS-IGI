from django.contrib import admin
from app.app_models.orderModels import Order, OrderInfo


class OrderInfoInline(admin.TabularInline):
    model = OrderInfo


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_id', 'display_books',
                    'created_at', 'updated_at')
    list_filter = ['customer_id']
    inlines = [OrderInfoInline]
    fieldsets = (
        (None, {
            'fields': ['customer_id', 'goods']
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )

    def display_books(self, obj):
        return ' '.join([f'{book.id} {book.title} {book.author.surname} {book.price}' for book in obj.goods.all()])


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'delivery_date', 'delivery_address',
                    'order_price', 'status', 'sale', 'created_at', 'updated_at')
    list_filter = ('order_id', 'delivery_date', 'delivery_address',
                   'order_price', 'status', 'sale')
    fieldsets = (
        (None, {
            'fields': ('order_id', 'delivery_date', 'delivery_address', 'order_price', 'status', 'sale')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )
