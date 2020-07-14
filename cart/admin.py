from django.contrib import admin

# Register your models here.
from cart.models import Cart, Order

admin.site.register(Cart)
admin.site.register(Order)
