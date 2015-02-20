from django.conf.urls import patterns, url
from main import views
# above is for django stuffs
# below is for serving static files for developments
# not used in live production
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
