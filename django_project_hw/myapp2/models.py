from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Username: {self.name}, email: {self.email}, phone number: {self.phone_number}, '
                f'address: {self.address}, register date:{self.register_date}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()
    adding_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Username: {self.name}, description: {self.description}, price: {self.price}, '
                f'address: {self.quantity}, register date:{self.adding_date}')


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    ordering_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'client_id: {self.client_id}, product_id: {self.product_id}, total price: {self.total_price}, '
                f'ordering date: {self.ordering_date}')
