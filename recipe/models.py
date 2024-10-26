from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100)

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField()

class Warehouse(models.Model):
    raw_material = models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    remaining_quantity = models.FloatField()
    price = models.FloatField()

