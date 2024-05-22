from order.models import ShopCartForm
from .models import Product, Category
from django.shortcuts import render, get_object_or_404

def products_view(request, category_id=None):
    categories = Category.objects.filter(status=True, parent=None).order_by('order')
    subcategories = Category.objects.filter(status=True).exclude(parent=None).order_by('order')
    
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category__in=selected_category.get_descendants(include_self=True))
    else:
        products = Product.objects.all()
    
    data = {
        "products": products,
        "categories": categories,
        "subcategories": subcategories,
        "selected_category": selected_category if category_id else None
    }
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


