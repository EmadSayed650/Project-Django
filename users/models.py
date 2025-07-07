from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def is_manager(self):
        return self.role == 'manager'

    def is_employee(self):
        return self.role == 'employee'
