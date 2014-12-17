from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User

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

		
		
	def testMainViewShowsUserInfo(self):
		c = Client()
		c.login(username='sashko', password='poland')
		response = c.get(reverse('main'))
		self.assertContains(response,"Name: Olexandr")
		self.assertContains(response,"Surname: Lykhenko")
		self.assertContains(response,"Email: lykhenko.olexandr@gmail.com") 

	def testUserHasNeededProfileAttributes(self):
		u = User.objects.get(username='sashko')
		up = UserProfile.objects.get(user=u)
		self.assertEquals(hasattr(u,'userprofile'),True)
		self.assertEquals(hasattr(u.userprofile, 'bio'),True)
		# self.assertEquals(hasattr(u, 'jabber',True))
		# self.assertEquals(hasattr(u, 'skype',True))
		# self.assertEquals(hasattr(u, 'other_contacts',True))
		# self.assertEquals(hasattr(u, 'birth_date',True))

