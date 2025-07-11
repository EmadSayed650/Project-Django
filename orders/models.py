from django.db import models
import uuid
from users.models import CustomUser  

class Supermarket(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"Supermarket {self.id}: {self.name} located at {self.location}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled')
    ]

    order_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='created_orders')
    confirmed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='confirmed_orders')

    def __str__(self):
        return f"Order {self.order_id} by {self.created_by} - {self.status}"
