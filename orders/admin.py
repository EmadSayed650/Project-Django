from django.contrib import admin

# Register your models here.
from .models import Supermarket, Order

admin.site.register(Supermarket)
admin.site.register(Order)