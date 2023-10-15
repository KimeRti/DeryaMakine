from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='order'),
    path('add/<int:proid>', views.shop_cart_add, name='shop_cart_add'),
    path('delete/<int:id>', views.shop_cart_delete, name='deletefromcart'),
    path('checkout/', views.checkout, name='checkout'),
    path('ok-url/', views.ok_url, name='ok_url'),
    path('fail-url/', views.fail_url, name='fail_url'),
    path('payment/', views.payment, name='payment'),
]