from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.hello import views


urlpatterns = patterns('',
    url(r'^$',views.main,name='main'),
)