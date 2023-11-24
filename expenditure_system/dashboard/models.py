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
