from django.urls import path, include
from django.shortcuts import render
from .models import Order
from django.core.paginator import Paginator
# Create your views here.


def order_list(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 10)  # Show 10 orders per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders/orders.html', {'page_obj': page_obj})
