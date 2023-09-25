from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, Category


def products_view(request):
    data = {
        "products": Product.objects.all(),
        "categories": Category.objects.filter(status=True, parent=None),
        "subcategories": Category.objects.filter(status=True).exclude(parent=None)
    }
    return render(request, "products/products_1.html", data)



