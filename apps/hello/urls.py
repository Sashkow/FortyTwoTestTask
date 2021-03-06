from django.conf.urls import patterns, url
from apps.hello import views


urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^show_first_requests/$', \
        views.showFirstRequests, name='show-first-requests'),
    url(r'^show_django_settings/$', \
        views.showDjangoSettings, name='show-django-settings'),
    url(r'^edit_user_info/$', \
        views.editUserInfo, name='edit-user-info'),
)
