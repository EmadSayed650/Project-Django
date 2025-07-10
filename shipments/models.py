from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
    ]

    factory_name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    shipment_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.factory_name} - {self.item_name}"
