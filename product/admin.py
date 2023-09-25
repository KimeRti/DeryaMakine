from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status')
    list_filter = ('category', 'status')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
