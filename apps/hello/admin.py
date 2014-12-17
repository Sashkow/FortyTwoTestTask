from django.contrib import admin

from apps.hello.models import UserProfile

admin.site.register(UserProfile)
