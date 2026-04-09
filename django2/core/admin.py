from django.contrib import admin

from core.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'slug','created_at', 'modified_at', 'active']