from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = "PLANdesk Inventory Manager"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'category')
    list_filter = ('category', 'name')

# Register your models here.
admin.site.register(Product, ProductAdmin)
#admin.site.unregister(Group)