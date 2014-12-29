
from django.contrib.auth.views import redirect_to_login

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import RequestInfo, UserProfile
from django.contrib import auth
from django.contrib.auth import authenticate

from django.conf import settings
from django.template import loader
from django.template import RequestContext, Context
# from django.core.exceptions import DoesNotExist

from apps.hello.forms import UserProfileMultiForm, UserProfileForm, UserForm

from django.utils.safestring import mark_safe

from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def main(request):
    u = get_user_or_auth_and_get_admin(request)
    template_name = 'hello/index.html'
    context = {'u': u}
    return render(request, template_name, context)


def showFirstRequests(request):
    template_name = 'hello/firstrequests.html'
    requests = RequestInfo.objects.all()[:10]
    context = {'requests': requests}
    return render(request, template_name, context)

def addDjangoSettingscontextProcessor(request):
    return {
        'django_settings': settings,
    }

def showDjangoSettings(request):
    template_name = 'hello/showdjangosettings.html'
    c = RequestContext(request, {}, \
        processors=[addDjangoSettingscontextProcessor])
    
    return render(request,template_name,c)


##########################################
#5
##########################################

def editUserInfo(request):
    user = get_user_or_auth_and_get_admin(request)
    userprofile = get_or_create_user_profile(request)
    model_instances = {'user': user, 'profile': userprofile}
    if request.method == 'POST':
        form = UserProfileMultiForm(request.POST, request.FILES, instance=model_instances)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        form = UserProfileMultiForm(instance=model_instances)
    ava_url = settings.MEDIA_URL + str(form['profile']['ava'].value())
    return render(request, 'hello/editform.html', {'form': form, 'ava_url':ava_url})

def thanks(request):
    return HttpResponse('thanks!')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('main'))
    else:
        form = AuthenticationForm()
    return render(request, 'hello/login.html', {'form': form, 'django_settings': settings})    


###########################################
#util functions
##############################################

def get_user_or_auth_and_get_admin(request):
    """retunrs not lazy user object"""
    userLazySimpleObject = request.user
    try:
        u = User.objects.get(id=userLazySimpleObject.id)
    except User.DoesNotExist:
        print "Handling unauthorized user", User.DoesNotExist
        u = authenticate(username='admin', password='admin')
           
        auth.login(request, u)
    finally:
        return u

def get_or_create_user_profile(request):
    profile = None
    user = get_user_or_auth_and_get_admin(request)
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)
        profile.save()
    return profile




