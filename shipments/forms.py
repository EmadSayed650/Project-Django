from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['factory_name', 'item_name', 'quantity', 'shipment_date']
