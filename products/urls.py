from django.urls import path
from . import views

urlpatterns = [
    # عرض قائمة المنتجات العامة
    path('', views.product_list, name='product_list'),

    # إضافة منتج جديد (مدير فقط)
    path('create/', views.product_create, name='product_create'),

    # تعديل منتج (مدير فقط)
    path('update/<int:pk>/', views.product_update, name='product_update'),

    # عرض المخزون للموظف
    path('inventory/employee/', views.employee_inventory, name='employee_inventory'),

    # عرض المخزون للمدير + الطلبات المعلقة
    path('inventory/manager/', views.manager_inventory, name='manager_inventory'),

    # الموظف يرسل طلب لمنتج معين
    path('inventory/request/<int:product_id>/', views.create_product_request, name='create_product_request'),

    # المدير يوافق على الطلب
    path('request/approve/<int:request_id>/', views.approve_request, name='approve_request'),

    # المدير يرفض الطلب
    path('request/reject/<int:request_id>/', views.reject_request, name='reject_request'),
    # الحصول على تفاصيل منتج معين (AJAX)
    path('get/<int:pk>/', views.get_product, name='get_product'),

]


