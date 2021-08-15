from django.contrib import admin
from . models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display= ['name', 'category', 'price']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Customer)