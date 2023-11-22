from django.db import models
# from django.contrib.auth.models import 

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
        return self.name


# # quantity model
# class Quantity(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
#     staff = models.ForeignKey(User, models.CASCADE, null=True)
#     quantity = models.PositiveIntegerField(null=True)
#     date = models.DateField(auto_now_add=True, null=True)
#     total = models.PositiveIntegerField(null=True)
    
#     class Meta:
#         verbose_name_plural = 'Quantity'
    
#     def __str__(self):
#         return f'{self.item} - {self.staff.username} - {self.quantity}'