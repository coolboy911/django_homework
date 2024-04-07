from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = 'create a client using arguments (name), (email), (phone_number), (address)'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='name')
        parser.add_argument('email', type=str, help='email')
        parser.add_argument('phone_number', type=str, help='phone number')
        parser.add_argument('address', type=str, help='address')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_number = kwargs.get('phone_number')
        address = kwargs.get('address')
        client = Client(name=name, email=email, phone_number=phone_number, address=address)
        client.save()
        self.stdout.write(f'{client} was created')
