from django import forms
from django.forms import formset_factory

from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)


ProductFormSet = formset_factory(ProductForm, extra=5)
ProductImageFormSet = formset_factory(ProductImageForm, extra=5)