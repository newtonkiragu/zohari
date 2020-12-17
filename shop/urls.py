from django.conf.urls import url
from django.urls import path

from cart.views import add_to_cart, remove_from_cart, decrease_cart
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.HomePageView.as_view(), name='landing_page'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('profile/<username>/', views.profile, name='profile'),
    path('accounts/register/', views.SignUpView.as_view(), name='signup'),
    path('cart/<slug>/', add_to_cart, name='add-to-cart'),
    # url('^cart/$', add_to_cart, name='cart'),
    path('product/<slug>/', views.product_detail, name='product-detail'),
    path('cart/decrease/<slug>/', decrease_cart, name='decrease-cart'),
    path('remove/<slug>/', remove_from_cart, name='remove-cart'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('shop/', views.ProductListView.as_view(), name="product-list"),
    path('activate/<uidb64>/<token>/', views.ActivateAccount.as_view(), name='activate'),
]

if settings.DEBUG: 
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)