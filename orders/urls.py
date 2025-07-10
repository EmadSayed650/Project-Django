from .views import order_list,create_order
from django.urls import path, include
urlpatterns = [
    path('', order_list, name='order_list'),
    path('create/', create_order, name='create_order'),
]
