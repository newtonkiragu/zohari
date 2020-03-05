from django.contrib import admin

from cart.models import Order, Cart

admin.site.register(Cart)
admin.site.register(Order)
