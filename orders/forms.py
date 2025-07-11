from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supermarket'] 

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['supermarket'].widget.attrs.update({
            'class': 'w-full px-3 py-2 bg-gray-700 text-white rounded-md'
        })


class ConfirmOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super(ConfirmOrderForm, self).__init__(*args, **kwargs)
        allowed_statuses = ['Confirmed', 'Shipped', 'Delivered', 'Cancelled']
        self.fields['status'].choices = [
            (status, status) for status in allowed_statuses
        ]
        self.fields['status'].widget.attrs.update({
            'class': 'w-full p-2 bg-gray-800 text-white rounded'
        })

    def clean_status(self):
        status = self.cleaned_data.get('status')
        allowed_statuses = ['Confirmed', 'Shipped', 'Delivered', 'Cancelled']
        if status not in allowed_statuses:
            raise forms.ValidationError("You are only allowed to update the status to a valid state.")
        return status
