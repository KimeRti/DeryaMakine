from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product

    @property
    def amount(self):
        return self.quantity * self.product.price


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
        widgets= {
            'quantity': TextInput(attrs={'class': 'input', 'type': 'number', 'value': 1}),
        }


"""class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    shipname = models.CharField(max_length=20)
    shipaddress = models.CharField(max_length=150)
    shipphone = models.CharField(max_length=20)
    total = models.FloatField()
    note = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.shipname"""
