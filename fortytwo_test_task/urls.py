from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.hello import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', include("apps.hello.urls")),
    url(r'^$', views.main, name='main'),
)
