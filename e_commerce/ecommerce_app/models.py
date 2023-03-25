from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    cost = models.PositiveIntegerField(default=1)
    img = models.ImageField(null=True, max_length=500)

    def __str__(self) -> str:
        return f"{self.name} {self.category} {self.cost} {self.img}"


class Shopping_cart(models.Model):
     product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True) 
     quantity = models.IntegerField(default=1)

     def __str__(self) -> str:
        return f"{self.product} {self.quantity}"