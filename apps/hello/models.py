"""models"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    jabber = models.CharField(max_length=50, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    other_contacts = models.TextField(null=True, blank=True)
    ava  = models.FileField(null=True, blank=True, upload_to=content_file_name)


class RequestInfo(models.Model):
    pickled_request = models.TextField(default="Empty")
    pub_date = models.DateTimeField('date published', default=timezone.now())

    def __str__(self):
        return str(self.pub_date) + " " + \
         str(self.pickled_request)[:100] + "..."

