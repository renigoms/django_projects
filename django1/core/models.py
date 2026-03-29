from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=10)
    stock_quantity = models.IntegerField('stock_quantity')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField('name', max_length=100)
    email = models.EmailField('email', max_length=100)
    surname = models.CharField('surname', max_length=100)

    def __str__(self):
        return f'{self.name} {self.surname}'
