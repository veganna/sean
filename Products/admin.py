from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["__str__", "product_SKU", "product_sale_price"]
    list_filter = ["product_is_OEM", "is_active"]
    search_fields = ["product_name", "product_SKU"]
