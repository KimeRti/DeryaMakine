from django.shortcuts import render


def home_view(request):
    return render(request, "main/index.html")


def about_view(request):
    return render(request, "main/about.html")


def contact_view(request):
    return render(request, "main/contact.html")







