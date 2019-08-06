from django.contrib import admin
from shop.models import Category, Product, CartItem, Cart

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)