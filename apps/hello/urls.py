from django.conf.urls import patterns, url
from apps.hello import views



urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^show_first_requests/$', views.showFirstRequests, name='show-first-requests'),
)
