from django.db import models
import uuid
# Create your models here.

class Supermarket(models.Model):
    name = models.CharField(max_length=255)
    
class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending')
    # created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='created_orders')
    # confirmed_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='confirmed_orders')
