from django.db import models
from django.contrib.auth.models import User


CATEGORY = (
    ('Food', 'Food'),
    ('Clothes', 'Clothes'),
    ('Stationary', 'Stationary'),
    ('Others', 'Others'),
)


# item model

class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    price = models.PositiveIntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Item'

    def __str__(self):
        return f'{self.name}'


# quantity model
class Quantity(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.PositiveIntegerField(null=True)
    date = models.DateField(auto_now_add=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY, null=True)
    total = models.PositiveIntegerField(null=True)
    
    class Meta:
        verbose_name_plural = 'Item Details'
    
    def __str__(self):
        return f'{self.item} - {self.quantity} - {self.price} - {self.category} - {self.date} - {self.staff.username} - {self.total}'
