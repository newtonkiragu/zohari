from django import template
from shop.models import Category, Product

register = template.Library()


@register.filter
def category_lists():
    category = Category.objects.all()

    if category.exists():
        return category
    else:
        return "No Categories found"


@register.filter
def category_product_filter():
    pass
