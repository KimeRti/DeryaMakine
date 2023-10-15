from django.contrib import admin
from order.models import ShopCart, Order, OrderDetail

admin.site.register(ShopCart)
admin.site.register(Order)
admin.site.register(OrderDetail)
