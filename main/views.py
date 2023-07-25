from django.shortcuts import render


def home_view(request):
    return render(request, "main/index.html", {'url': 'home'})


def about_view(request):
    return render(request, "main/About.html", {'url': 'about'})


def contact_view(request):
    return render(request, "main/contact.html", {'url': 'contact'})







