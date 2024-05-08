from django.contrib import admin
from app.app_models.customerModel import Customer, CustomerReview


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'password',
                    'created_at', 'updated_at')
    list_filter = ('name', 'phone', 'email', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'email', 'password')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )


@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'rate', 'text',
                    'created_at', 'updated_at')
    list_filter = ('user', 'rate', 'text', 'created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'rate', 'text')
        }),
        ('Object info', {'fields': ['created_at', 'updated_at']})
    )
