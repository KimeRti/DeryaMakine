from order.models import ShopCartForm
from .models import Product, Category
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
import json
from django.db.models import Q

def products_view(request, category_id=None):
    selected_category = None
    subcategories = []
    products = []

    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        subcategories = Category.objects.filter(parent=selected_category)
        if not subcategories:
            products = Product.objects.filter(category=selected_category)
    else:
        products = Product.objects.all()

    categories = Category.objects.filter(status=True, parent=None).order_by('order')
    all_subcategories = {category.id: list(Category.objects.filter(parent=category).order_by('order').values('id', 'title', 'slug')) for category in categories}

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'subcategories': subcategories,
        'all_subcategories': json.dumps(all_subcategories)
    }
    return render(request, 'products/products_1.html', context)


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
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) | Q(keywords__icontains=query)
        )
    else:
        products = Product.objects.none()
    
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

