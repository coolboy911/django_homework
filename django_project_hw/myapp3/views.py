from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from myapp2.models import Order, Product


# Create your views here.

def last_order_products(request, client_id, argument):
    start_time = datetime.now()
    minus_days = 0
    if argument == 'year':
        minus_days = 365
    elif argument == 'month':
        minus_days = 30
    elif argument == 'week':
        minus_days = 7
    start_time -= timedelta(days=minus_days)

    order_list = Order.objects.filter(client_id__pk=client_id).filter(ordering_date__gte=start_time).order_by(
        '-ordering_date')
    products_list = []
    for order in order_list:
        for product in order.product_id.all():
            if product not in products_list:
                products_list.append(product)

    context = {'client_id': client_id, 'product_list': products_list}
    return render(request, 'myapp3/client_products.html', context=context)
