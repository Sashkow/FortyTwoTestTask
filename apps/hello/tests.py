from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User

# Create your tests here.
class SomeTests(TestCase):
    def test_math(self):
        assert(2+2==4)

class MainViewTests(TestCase):
	fixtures =['hello_main_view_testdata.json']

	def __init__(self, *args, **kwargs):
		super(TestCase, self).__init__(*args, **kwargs)
		# self.gen_stubs()

		self.c = Client()
		self.c.login(username='sashko', password='poland')
		
	def testMainViewShowsUserInfo(self):
		response = self.c.get(reverse('main'))
		print '-->', response, '<--'
		self.assertContains(response,"Name: Olexandr")
		self.assertContains(response,"Surname: Lykhenko")
		self.assertContains(response,"Email: lykhenko.olexandr@gmail.com") 

	def testUserHasNeededProfileAttributes(self):
		u = User.objects.get(username='sashko')
		self.assertEquals(hasattr(u, 'bio'),True)
		self.assertEquals(hasattr(u, 'jabber',True))
		self.assertEquals(hasattr(u, 'skype',True))
		self.assertEquals(hasattr(u, 'other_contacts',True))
		self.assertEquals(hasattr(u, 'birth_date',True))

