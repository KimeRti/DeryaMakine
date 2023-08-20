from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductImageForm, ProductImageFormSet, ProductFormSet
from .models import Product, ProductImage


def products_view(request):
    data = {
        "products": Product.objects.all(),
    }
    return render(request, "products/products_1.html", data)


def add_product(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        image_formset = ProductImageFormSet(request.POST, request.FILES, prefix='image')

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            for form in image_formset:
                if form.cleaned_data.get('image'):
                    image = form.save(commit=False)
                    image.product = product
                    image.save()
            return redirect('products')
    else:
        product_form = ProductForm()
        image_formset = ProductImageFormSet(prefix='image')

    return render(request, 'products/add_product.html', {'product_form': product_form, 'image_formset': image_formset})


def product_detail(request, pk):
    data = {
        "product": Product.objects.get(id=pk),
        "images": ProductImage.objects.filter(product=pk)
    }
    return render(request, "products/product_details.html", data)
