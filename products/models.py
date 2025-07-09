from django.db import models
from django.db.models import PositiveIntegerField
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    critical_amount = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.name