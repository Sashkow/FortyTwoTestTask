from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def main(request):
 	userLazySimpleObject = request.user 
	u = User.objects.get(id=userLazySimpleObject.id)

	return HttpResponse( \
		"Name: {name} Surname: {surname} Email: {email}". \
		format(name = u.first_name,surname = u.last_name, email = u.email))