from django.contrib import admin
from shop.models import Brand, Category, Images, Product
# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Product)