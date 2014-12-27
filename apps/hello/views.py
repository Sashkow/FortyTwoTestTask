


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from models import RequestInfo, UserProfile
from django.contrib.auth import authenticate, login

from django.conf import settings
from django.template import loader
from django.template import RequestContext, Context
# from django.core.exceptions import DoesNotExist

from apps.hello.forms import UserProfileMultiForm, UserProfileForm, UserForm

from django.utils.safestring import mark_safe

def getUserOrAuthAndGetAdmin(request):
    userLazySimpleObject = request.user
    try:
        u = User.objects.get(id=userLazySimpleObject.id)
    except User.DoesNotExist:
        print "Handling unauthorized user", User.DoesNotExist
        u = authenticate(username='admin', password='admin')
        login(request, u)
    finally:
        return u

# Create your views here.
def main(request):
    u = getUserOrAuthAndGetAdmin(request)
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
    user = getUserOrAuthAndGetAdmin(request)
    if request.method == 'POST':
        form = UserProfileMultiForm(request.POST,instance={
            'user': user,
            'profile': user.userprofile,
            })
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('main'))
    else:
        form = UserProfileMultiForm(instance={
            'user': user,
            'profile': user.userprofile,
            })
    context = Context({'form': form})
    return render(request, 'hello/editform.html', context)

def thanks(request):
    return HttpResponse('thanks!')
