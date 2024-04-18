from django.shortcuts import render
from django.shortcuts import render, redirect

from order.models import ShopCartForm
from .models import Product, Category


def products_view(request):
    data = {
        "products": Product.objects.all(),
        "categories": Category.objects.filter(status=True, parent=None),
        "subcategories": Category.objects.filter(status=True).exclude(parent=None)
    }
    p = Product.objects.get(id=1)
    print(p.image.url)
    return render(request, "products/products_1.html", data)


def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    form = ShopCartForm()
    url = 'products'
    data = {
        "product": product,
        "url": url,
        "form": form
    }
    return render(request, "products/product_details.html", data)


