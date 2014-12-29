from betterforms.multiform import MultiModelForm
from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User
from models import RequestInfo, UserProfile





class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['birth_date','bio', 'jabber','skype','other_contacts','ava']

class UserProfileMultiForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'profile': UserProfileForm,
    }

    # def __init__(self,*args, **kwargs):
    #     try:
    #         if not 'instance' in kwargs:
    #             raise KeyError('UserProfileMultiForm class needs "instance" argument')
    #     except KeyError as inst:
    #         print inst.args[0]
    #         raise
    #     super(UserProfileMultiForm, self).__init__(*args, **kwargs)


    # def save(self, commit=True):
    #     objects = super(UserProfileMultiForm, self).save(commit=False)

    #     if commit:
    #         user = objects['user']
    #         user.save()
    #         profile = objects['profile']
    #         profile.user = user
    #         profile.save()

    #     return objects
