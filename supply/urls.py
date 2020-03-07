from django.conf.urls import url

from cart.views import add_to_cart, remove_from_cart, decrease_cart
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.HomePageView.as_view(), name='landing_page'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about'),
    url(r'^profile/(?P<username>\w+)$', views.profile, name='profile'),
    url(r'^accounts/register/$', views.signup, name='signup'),
    url('^cart/(?P<slug>.+)$', add_to_cart, name='cart'),
    url(r'product/(?P<slug>.+)$', views.ProductDetail.as_view(), name='product-detail'),
    url(r'cart/decrease/(?P<slug>.+)$', decrease_cart, name='decrease-cart'),
    url(r'^remove/(?P<slug>.+)$', remove_from_cart, name='remove-cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
