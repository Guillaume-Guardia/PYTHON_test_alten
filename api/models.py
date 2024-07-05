from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    inventory_status = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
