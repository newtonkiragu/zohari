from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^cart/$', views.cart_view, name='cart-home'),
]
