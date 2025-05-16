from django.db import models
from customers.models import Customer

# Create your models here.

class Offer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'Ponuda {self.id} za {self.customer.name}'