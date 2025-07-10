# shipments/urls.py

from django.urls import path
from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.shipment_list, name='shipment_list'),
    path('shipments/add/', views.add_shipment, name='add_shipment'),
    path('shipments/confirm/<int:shipment_id>/', views.confirm_shipment, name='confirm_shipment'),
    path('edit/<int:shipment_id>/', views.edit_shipment, name='edit_shipment'),

]
