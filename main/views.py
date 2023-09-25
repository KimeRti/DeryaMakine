from django.shortcuts import render

from product.models import Category


def home_view(request):
    category = Category.objects.filter(status=True)
    return render(request, "main/index.html", {'url': 'home', 'category': category})


def about_view(request):
    return render(request, "main/about.html", {'url': 'about'})


def contact_view(request):
    return render(request, "main/contact.html", {'url': 'contact'})


def brands_view(request):
    return render(request, "main/brands.html", {'url': 'brands'})


def privacy_view(request):
    return render(request, "main/privacy.html", {'url': 'privacy'})


def terms_view(request):
    return render(request, "main/terms.html", {'url': 'terms'})


def usage_view(request):
    return render(request, "main/usage.html", {'url': 'usage'})









