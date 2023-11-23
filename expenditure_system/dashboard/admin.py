from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from user.models import Profile

# title of the admin page
admin.site.site_header = 'Expenditure Management System'


# display table form the item table in the admin panel
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'category')
    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'price')
        }),
    )

class QuantityAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price', 'category', 'date', 'staff', 'total')
    list_filter = ('category', 'date', 'staff')
    search_fields = ('item', 'category', 'staff')
    list_per_page = 10
    ordering = ('item',)
    
    fieldsets = (
    (None, {
        'fields': ('item', 'staff','quantity', 'price', 'category', 'total')
    }),
    )


# Register your models here.
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Quantity, QuantityAdmin)

# unregister the Group model from admin.
admin.site.unregister(Group)
