from django.contrib import admin
from .models import Item, Quantity
from django.contrib.auth.models import Group

# header customization
admin.site.site_header = 'Expenditure System'

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category', 'price')
    list_per_page = 10
    
class QuantityAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price', 'category', 'date', 'staff', 'total')
    list_filter = ('category', 'date', 'staff')
    search_fields = ('item', 'category', 'staff')
    list_per_page = 10

# item model
admin.site.register(Item, ItemAdmin)

# quantity model
admin.site.register(Quantity, QuantityAdmin)


# unregister the Group model from admin.
admin.site.unregister(Group)
