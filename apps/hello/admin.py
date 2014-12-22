from django.contrib import admin

from apps.hello.models import UserProfile
from apps.hello.models import RequestInfo	

admin.site.register(UserProfile)
admin.site.register(RequestInfo)
