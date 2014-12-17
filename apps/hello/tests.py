from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client

# Create your tests here.
class SomeTests(TestCase):
    def test_math(self):
        assert(2+2==4)

class MainViewTests(TestCase):
	fixtures =['hello_main_view_testdata.json']

	def testMainViewShowsUserInfo(self):
		c = Client()
		c.login(username='sashko', password='poland')
		response = c.get(reverse('main'))
		print '-->', response, '<--'
		self.assertContains(response,"Name: Olexandr")
		self.assertContains(response,"Surname: Lykhenko")
		self.assertContains(response,"Email: lykhenko.olexandr@gmail.com") 
