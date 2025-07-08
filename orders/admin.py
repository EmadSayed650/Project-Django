from django.contrib import admin

# Register your models here.

from .models import Order, Supermarket

admin.site.register(Order)
admin.site.register(Supermarket)
