from django.conf.urls import url

from cart.views import add_to_cart, remove_from_cart
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.HomePageView.as_view(), name='landing_page'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^accounts/register/$', views.signup, name='signup'),
    url('cart/(?P<slug>\w+)', add_to_cart, name='cart'),
    url('remove/(?P<slug>\w+)', remove_from_cart, name='remove-cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
