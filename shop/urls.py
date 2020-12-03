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
    url('^cart/(?P<slug>.+)$', add_to_cart, name='add-to-cart'),
    # url('^cart/$', add_to_cart, name='cart'),
    url(r'product/(?P<slug>.+)$', views.ProductDetail.as_view(), name='product-detail'),
    url('cart/decrease/(?P<slug>.+)$', decrease_cart, name='decrease-cart'),
    url(r'^remove/(?P<slug>.+)$', remove_from_cart, name='remove-cart'),
    url('search/', views.SearchResultsView.as_view(), name='search_results'),
    url('shop/', views.ProductListView.as_view(), name="product-list")
]

