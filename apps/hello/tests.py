from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User
from datetime import date

from apps.hello.models import UserProfile

# Create your tests here.
class SomeTests(TestCase):
    def test_math(self):
        assert(2+2==4)

class MainViewTests(TestCase):
	fixtures =['hello_main_view_testdata.json']

	def __init__(self, *args, **kwargs):
		super(TestCase, self).__init__(*args, **kwargs)
		# self.gen_stubs()

	def testUserHasNeededProfileAttributes(self):
		u = User.objects.get(username='sashko')
		up = UserProfile.objects.get(user=u)
		self.assertEquals(hasattr(u,'userprofile'),True)
		self.assertEquals(hasattr(u.userprofile, 'bio'),True)
		self.assertEquals(hasattr(u.userprofile, 'jabber'),True)
		self.assertEquals(hasattr(u.userprofile, 'skype'),True)
		self.assertEquals(hasattr(u.userprofile, 'other_contacts'),True)
		self.assertEquals(hasattr(u.userprofile, 'birth_date'),True)	
		
	def testMainViewShowsUserInfo(self):
		c = Client()
		c.login(username='sashko', password='poland')
		response = c.get(reverse('main'))
		self.assertContains(response,"Name: Olexandr")
		self.assertContains(response,"Surname: Lykhenko")
		self.assertContains(response,"Birth date: "+str(date(1991, 1, 2))) 
		self.assertContains(response,"Bio: Born") 
		self.assertContains(response,"Jabber: sashko@jabber") 
		self.assertContains(response,"Skype:") 
		self.assertContains(response,"Other contacts: contacts") 
		

	

