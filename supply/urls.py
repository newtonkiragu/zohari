from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.index, name='mainPage'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^accounts/register/$', views.signup, name='signup'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
