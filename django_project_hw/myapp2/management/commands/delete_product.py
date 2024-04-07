from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = 'Delete proudct by id.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        product.delete()
        self.stdout.write(f'{product} was deleted')
