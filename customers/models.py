from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=20)  # OIB tvrtke
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    name = models.CharField(max_length=150,
                             null=False,
                             blank=False)
    vat_id = models.TextField(max_length=10,
                              null=False,
                                blank=False)
    street = models.CharField(max_length=150,
                              null=True,
                              blank=True)

    city = models.CharField(max_length=150,
                              null=True,
                              blank=True,)
    country = models.CharField(max_length=150,
                              null=True,
                              blank=True,)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f'{self.name} - ({self.vat_id})'

    