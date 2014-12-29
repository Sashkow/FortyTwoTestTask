from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.hello import views

from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()
print admin.__file__
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', include("apps.hello.urls")),
    url(r'^$', views.main, name='main'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
