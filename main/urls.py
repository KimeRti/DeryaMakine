from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('index.html',views.home_view,name="home"),
    path("about", views.about_view ,name="about"),
    path("contact", views.contact_view ,name="contact"),
    path("brands", views.brands_view ,name="brands"),
    path("privacy", views.privacy_view ,name="privacy"),
    path("terms", views.terms_view ,name="terms"),
    path("usage", views.usage_view ,name="usage"),
]