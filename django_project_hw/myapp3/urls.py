from django.urls import path
from . import views

urlpatterns = [
    path('<int:client_id>/last_week', views.last_order_products, {'argument': 'week'}, name='last_week'),
    path('<int:client_id>/last_month', views.last_order_products, {'argument': 'month'}, name='last_week'),
    path('<int:client_id>/last_year', views.last_order_products, {'argument': 'year'}, name='last_week'),
    path('add_product', views.add_product, name='add_product')
]
