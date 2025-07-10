from django.contrib import admin
from .models import Product, ProductRequest

# تسجيل الموديلات
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'critical_amount')
    search_fields = ('name',)


@admin.register(ProductRequest)
class ProductRequestAdmin(admin.ModelAdmin):
    list_display = ('product', 'employee', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('product__name', 'employee__username')
