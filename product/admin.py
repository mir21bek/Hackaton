from django.contrib import admin
from .models import Product,Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','price']
    list_filter = ['category']



admin.site.register(Product,ProductAdmin)
