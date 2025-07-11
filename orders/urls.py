# orders/urls.py

from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='order_list'),                        # صفحة عرض كل الطلبات
    path('create/', views.create_order, name='create_order'),            # صفحة إنشاء طلب جديد
    path('<uuid:order_id>/confirm/', views.confirm_order, name='confirm_order'),  # تأكيد الطلب (Manager فقط)
    path('<uuid:order_id>/edit/', views.edit_order, name='edit_order'),  # تعديل الطلب (Manager فقط)
]
