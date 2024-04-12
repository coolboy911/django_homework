from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from myapp2.models import Order, Product
from .forms import ProductForm


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


def add_product(request):
    title = "Товар"
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'не валидные данные'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            adding_date = form.cleaned_data['adding_date']
            picture = form.cleaned_data['picture']
            product = Product(name=name, description=description, price=price, quantity=quantity,
                              adding_date=adding_date, picture=picture)
            product.save()
            message = 'товар успешно добавлен'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp3/base_form.html',
                  {'form': form, 'title': title, 'message': message})
