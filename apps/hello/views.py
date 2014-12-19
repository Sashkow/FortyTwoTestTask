from django.shortcuts import render
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

# from django.core.exceptions import DoesNotExist


# Create your views here.
def main(request):
    userLazySimpleObject = request.user
    try:
        u = User.objects.get(id=userLazySimpleObject.id)
    except User.DoesNotExist:
        print "Handling unauthorized user", User.DoesNotExist
        u = authenticate(username='admin', password='admin')
        login(request, u)
    finally:
        template_name = 'hello/index.html'
        context = {'u': u}
        return render(request, template_name, context)
