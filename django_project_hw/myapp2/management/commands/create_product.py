from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = 'create a client using arguments (name), (description), (price), (quantity)'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name')
        parser.add_argument('description', type=str, help='description')
        parser.add_argument('price', type=float, help='price')
        parser.add_argument('quantity', type=int, help='quantity')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()
        self.stdout.write(f'{product} was created')
