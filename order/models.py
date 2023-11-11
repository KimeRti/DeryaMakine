from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

from product.models import Product


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

    @property
    def amount(self):
        return self.quantity * self.product.price


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
        widgets = {
            'quantity': TextInput(attrs={'class': 'input', 'type': 'number', 'value': 1}),
        }
        labels = {
            'quantity': 'Adet',
        }


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('OnShipping', 'OnShipping'),
        ('Completed', 'Completed'),
    )
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    note = models.TextField()
    status = models.CharField(choices=STATUS, default='New', max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'address', 'city', 'country', 'phone', 'note', 'email']
        widgets = {
            'name': TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'name', 'id': "name", 'placeholder': "İsim Girin", 'required': 'required'}),
            'surname': TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'surname', 'id': "surname", 'placeholder': "Soyisim Girin", 'required': 'required'}),
            'country': TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'country', 'id': "country", 'placeholder': "Ülke Girin", 'required': 'required'}),
            'city': TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'city', 'id': "city", 'placeholder': "Şehir Girin", 'required': 'required'}),
            'address': TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'address', 'id': "address", 'placeholder': "Adres Girin", 'required': 'required'}),
            'phone': TextInput(attrs={'type': 'tel', 'class': 'form-control', 'name': 'tel', 'id': "tel", 'placeholder': "Telefon Numarası Girin", 'required': 'required'}),
            'note': TextInput(attrs={'type': 'text', 'class': 'form-control', 'name': 'note', 'id': "note", 'placeholder': "Not Girin"}),
            'email': TextInput(attrs={'type': 'email', 'class': 'form-control', 'name': 'email', 'id': "email", 'placeholder': "Email Girin", 'required': 'required'}),
        }
        labels = {
            'name': 'İsim',
            'surname': 'Soyisim',
            'country': 'Ülke',
            'city': 'Şehir',
            'address': 'Adres',
            'phone': 'Telefon',
            'note': 'Not',
            'email': 'Email',
        }


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    total = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
