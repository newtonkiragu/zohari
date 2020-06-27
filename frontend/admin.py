from django.contrib import admin
from .models import Product, Profile, Brand, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Brand)
admin.site.register(Category)
