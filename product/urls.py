from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name="products"),
    path('productdetail/<int:pk>', views.product_detail_view, name='productdetail'),
]