from django.shortcuts import render


def products_view(request):
    return render(request, "products/products_1.html")

