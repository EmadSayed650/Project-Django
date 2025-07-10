from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supermarket', 'status']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['supermarket'].widget.attrs.update({
            'class': 'w-full px-3 py-2 bg-gray-700 text-white rounded-md'
        })
        self.fields['status'].widget.attrs.update({
            'class': 'w-full px-3 py-2 bg-gray-700 text-white rounded-md'
        })
