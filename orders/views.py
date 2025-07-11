from django.urls import path, include
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order
from .forms import OrderForm, ConfirmOrderForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test
def is_manager(user):
    return user.is_authenticated and user.role == 'manager'
def order_list(request):
    orders = Order.objects.all().order_by('-order_date')
    paginator = Paginator(orders, 10)  # Show 10 orders per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'orders/orders.html', {'page_obj': page_obj})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user
            order.status = 'Pending' 
            order.save()
            messages.success(request, "Order created successfully.")
            return redirect('orders:order_list')
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form})


@user_passes_test(is_manager)
def confirm_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)


   
    if order.status != 'Pending':
        messages.warning(request, 'This order is already confirmed or processed.')
        return redirect('orders:order_list')

    if request.method == 'POST':
        form = ConfirmOrderForm(request.POST, instance=order)
        if form.is_valid():
            confirmed_order = form.save(commit=False)
            confirmed_order.confirmed_by = request.user
            confirmed_order.save()
            messages.success(request, "Order confirmed successfully.")
            return redirect('orders:order_list')
    else:
        form = ConfirmOrderForm(instance=order)

    return render(request, 'orders/confirm_order.html', {'form': form, 'order': order})

# --------------------------------------------------------

@user_passes_test(is_manager)
def edit_order(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)


    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order updated successfully.')
            return redirect('orders:order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'orders/update_order.html', {'form': form})
