from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import login_view, logout_view, dashboard_view, create_employee_view
urlpatterns = [
    path('', lambda request: redirect('login')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create-employee/', create_employee_view, name='create_employee'),
    path('view-employees/', views.view_employees, name='view_employees'),
    path('employee/orders/', views.employee_orders, name='employee_orders'),
    path('employee/shipments/', views.employee_shipments, name='employee_shipments'),
    path('employee/inventory/', views.employee_inventory, name='employee_inventory'),
    path('manager/orders/', views.manager_orders, name='manager_orders'),
    path('manager/shipments/', views.manager_shipments, name='manager_shipments'),
    path('manager/inventory/', views.employee_inventory, name='manager_inventory'),
]
