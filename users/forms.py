# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'employee'  # تعيين الرول تلقائيًا
        if commit:
            user.save()
        return user
