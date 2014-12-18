from django.views.generic import DetailView

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
	finally:
		u = authenticate(username='sashko', password='poland')
		login(request, u)

	template_name = 'hello/index.html'

	context = {'u': u}

	return render(request,template_name,context)

	# return HttpResponse( \
	# 	"Name: {name} <br> Surname: {surname} <br> Email: {email} <br> \
	# 	 Birth date: {bd} <br> Bio: {bio} <br> Jabber: {j} <br> Skype: {s} <br> Other contacts: {othr}". \
	# 	format(name = u.first_name,surname = u.last_name, email = u.email, \
	# 	 bd=u.userprofile.birth_date, bio = u.userprofile.bio, j=u.userprofile.jabber, \
	# 	 s=u.userprofile.skype, othr=u.userprofile.other_contacts))

# class MainList(DetailView):
# 	model = User
# 	template_name = 'apps/hello/index.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(MainList, self).get_context_data(**kwargs)
# 		# context['now'] = timezone.now()
# 		print context
# 		return context
