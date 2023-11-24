from django import forms
from .models import Item, Quantity

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'price']