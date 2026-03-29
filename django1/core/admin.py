from django.contrib import admin

from core.models import Product, Client

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("stock_quantity","name", "price")

admin.site.register(Product, ProductAdmin)
admin.site.register(Client)
