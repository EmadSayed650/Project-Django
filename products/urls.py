from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.product_list, name='product_list'),

   
    path('create/', views.product_create, name='product_create'),

    
    path('update/<int:pk>/', views.product_update, name='product_update'),

    
    path('inventory/employee/', views.employee_inventory, name='employee_inventory'),

    
    path('inventory/manager/', views.manager_inventory, name='manager_inventory'),

    
    path('inventory/request/<int:product_id>/', views.create_product_request, name='create_product_request'),

    
    path('request/approve/<int:request_id>/', views.approve_request, name='approve_request'),

    
    path('request/reject/<int:request_id>/', views.reject_request, name='reject_request'),
   
    path('get/<int:pk>/', views.get_product, name='get_product'),

]


