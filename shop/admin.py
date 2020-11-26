from django.contrib import admin
from shop.models import Brand, Category, Images, Product
# Register your models here.

admin.site.Register(Brand)
admin.site.Register(Category)
admin.site.Register(Images)
admin.site.Register(Product)