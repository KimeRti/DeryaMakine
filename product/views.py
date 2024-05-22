from order.models import ShopCartForm
from .models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
import json

def products_view(request, category_id=None):
    categories = Category.objects.filter(status=True, parent=None).order_by('order')  # Sıralama
    all_subcategories = {category.id: list(Category.objects.filter(parent=category).order_by('order').values('id', 'title')) for category in categories}
    
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        subcategories = Category.objects.filter(parent=selected_category).order_by('order')
        if subcategories.exists():
            products = []
        else:
            products = Product.objects.filter(category=selected_category)
    else:
        selected_category = None
        subcategories = []
        products = Product.objects.all()
    
    data = {
        "products": products,
        "categories": categories,
        "subcategories": subcategories,
        "selected_category": selected_category,
        "all_subcategories": json.dumps(all_subcategories)
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

def search_results(request):
    query = request.GET.get('q')
    products = Product.objects.filter(title__icontains=query) if query else Product.objects.none()
    categories = Category.objects.filter(status=True, parent=None).order_by('order')
    all_subcategories = {category.id: list(Category.objects.filter(parent=category).order_by('order').values('id', 'title')) for category in categories}
    
    data = {
        'products': products,
        'categories': categories,
        'selected_category': None,
        'subcategories': [],
        'query': query,
        'all_subcategories': json.dumps(all_subcategories),
    }
    return render(request, 'products/products_1.html', data)

