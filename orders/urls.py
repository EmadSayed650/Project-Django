from .views import order_list
from django.urls import path, include
urlpatterns = [
    path('', order_list, name='order_list'),
]
