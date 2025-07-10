from django.urls import path, include
from django.shortcuts import redirect, render
from .models import Order
from django.core.paginator import Paginator
from .forms import OrderForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
# Create your views here.


def order_list(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 10)  # Show 10 orders per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders/orders.html', {'page_obj': page_obj})



def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user  # Assuming you have authentication set up
            order.status = 'pending'
            order.save()
            return redirect('order_list') 
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})




# def is_manager(user):
#     return user.is_authenticated and user.role == 'manager'

# @user_passes_test(is_manager)
# def confirm_order(request, order_id):
#     order = get_object_or_404(Order, id=order_id)
#     if request.method == 'POST':
#         form = ConfirmOrderForm(request.POST, instance=order)
#         if form.is_valid():
#             confirmed_order = form.save(commit=False)
#             confirmed_order.confirmed_by = request.user
#             confirmed_order.save()
#             return redirect('manager_dashboard')
#     else:
#         form = ConfirmOrderForm(instance=order)
#     return render(request, 'manager/confirm_order.html', {'form': form})