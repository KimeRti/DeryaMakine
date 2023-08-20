from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name="products"),
    path('add/', views.add_product, name="add_product"),
    path('detail/<int:pk>/', views.product_detail, name='product_detail'),
]