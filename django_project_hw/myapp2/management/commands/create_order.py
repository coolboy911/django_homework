from django.core.management.base import BaseCommand
from myapp2.models import Product, Order, Client


class Command(BaseCommand):
    help = ('create a order using arguments (client_id), ("product_id_1, product_id2, ..."), (total_price)'
            'example: python manage.py create_order 4 "1,1,1,2"')

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('products_id', type=str, help='products_id')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        products_id = kwargs['products_id'].split(',')
        client = Client.objects.filter(pk=client_id).first()
        if client:
            order = Order(client_id=client)
            order.save()
            for product_id in products_id:
                product = Product.objects.filter(pk=product_id).first()
                if product:
                    order.product_id.add(product)
                    order.total_price += product.price
                    order.save()

            self.stdout.write(f'{client_id} {products_id} was updated')
        else:
            self.stdout.write(f'client with id:{client_id} not found, aborting operation')

