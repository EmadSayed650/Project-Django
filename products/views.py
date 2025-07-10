from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product, ProductRequest
from .forms import ProductForm
from django.core.paginator import Paginator
from django.db.models import Q  # For search queries
from django.http import JsonResponse

# Helper function to check if user is a Manager
def is_manager(user):
    return user.role == 'manager' or user.groups.filter(name='Manager').exists()


# =======================
# صفحة عرض المنتجات العامة (للإدارة والموظفين) مع بحث وترقيم
# =======================

@login_required
def product_list(request):
    search_query = request.GET.get('q', '')  # Get search query
    products = Product.objects.all()

    if search_query:
        products = products.filter(Q(name__icontains=search_query))

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
    })

# =======================
# إضافة منتج جديد (للمدير فقط)
# =======================
@login_required
# @user_passes_test(is_manager)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            # AJAX Response
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('manager_inventory')
    return JsonResponse({'success': False, 'error': 'Invalid request'})


# =======================
# تعديل منتج (للمدير فقط)
# =======================
@login_required
@user_passes_test(is_manager)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('manager_inventory')
    return JsonResponse({'success': False, 'error': 'Invalid request'})


# =======================
# صفحة موظف: عرض المخزون مع بحث، ترقيم، طلب المنتجات الناقصة، عرض حالة الطلبات
# =======================

@login_required
def employee_inventory(request):
    search_query = request.GET.get('q', '')
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # طلبات الموظف الخاصة
    employee_requests = ProductRequest.objects.filter(employee=request.user).order_by('-created_at')

    # لو الموظف ضغط Add Product
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_inventory')
    else:
        form = ProductForm()

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'employee_requests': employee_requests,
        'form': ProductForm(),  # عشان نعرض الفورم
    }
    return render(request, 'products/employee_inventory.html', context)


# =======================
# إنشاء طلب منتج (من نفس صفحة employee_inventory)
# =======================
@login_required
def create_product_request(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 0))
        if quantity > 0:
            ProductRequest.objects.create(
                product=product,
                employee=request.user,
                quantity=quantity,
                status='pending'
            )
    return redirect('employee_inventory')

# =======================
# صفحة مدير: عرض المخزون مع بحث وترقيم، عرض الطلبات المعلقة
# =======================

@login_required
@user_passes_test(is_manager)
def manager_inventory(request):
    search_query = request.GET.get('q', '')
    products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    paginator = Paginator(products, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    pending_requests = ProductRequest.objects.filter(status='pending').order_by('-created_at')

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'pending_requests': pending_requests,
    }
    return render(request, 'products/manager_inventory.html', context)

# =======================
# الموافقة على طلب (للمدير فقط)
# =======================

@login_required
@user_passes_test(is_manager)
def approve_request(request, request_id):
    req = get_object_or_404(ProductRequest, id=request_id, status='pending')
    req.status = 'approved'
    req.save()
    # تحديث كمية المنتج عند الموافقة
    req.product.quantity += req.quantity
    req.product.save()
    return redirect('manager_inventory')

# =======================
# رفض طلب (للمدير فقط)
# =======================

@login_required
@user_passes_test(is_manager)
def reject_request(request, request_id):
    req = get_object_or_404(ProductRequest, id=request_id, status='pending')
    req.status = 'rejected'
    req.save()
    return redirect('manager_inventory')




@login_required
@user_passes_test(is_manager)
def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    data = {
        'id': product.id,
        'name': product.name,
        'quantity': product.quantity,
        'critical_amount': product.critical_amount,
    }
    return JsonResponse(data)