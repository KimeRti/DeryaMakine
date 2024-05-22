from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name="products"),
    path('search/', views.search_results, name='search_results'),
    path('productdetail/<int:pk>', views.product_detail_view, name='productdetail'),
    path('products/category/<int:category_id>/', views.products_view, name='products_by_category'),
]