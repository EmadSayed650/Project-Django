from django.urls import path, include
from django.shortcuts import render
# Create your views here.
def order_list(request):
    # This view will render a list of orders
    return render(request, 'orders/orders.html')
