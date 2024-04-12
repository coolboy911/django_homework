from django.contrib import admin
from .models import Client, Product, Order


# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов"""
    list_display = ['name', 'email', 'phone_number', 'address', 'register_date']
    ordering = ['-register_date']

    """Отдельный клиент"""
    fields = ['name', 'email', 'phone_number', 'address', 'register_date']
    readonly_fields = ['register_date']


class ProductAdmin(admin.ModelAdmin):
    """Список Товаров"""
    list_display = ['name', 'description', 'price', 'quantity', 'adding_date', 'picture']
    ordering = ['-adding_date']

    """Отдельный продукт"""
    fields = ['name', 'description', 'price', 'quantity', 'adding_date', 'picture']
    readonly_fields = ['adding_date']


class OrderAdmin(admin.ModelAdmin):
    # tweaking display of client
    # https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_display
    @admin.display(description='Client Email and address')
    def client_only_email(self, client):
        return f'{client.client_id.email} address: {client.client_id.address}'

    """Список Заказов"""
    list_display = ['client_only_email', 'total_price', 'ordering_date']
    ordering = ['-ordering_date']

    """Отдельный заказ"""
    readonly_fields = ['ordering_date']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
