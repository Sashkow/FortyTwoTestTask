from django.test import TestCase
from django.core.urlresolvers import reverse

# Create your tests here.
class SomeTests(TestCase):
    def test_math(self):
        assert(2+2==4)

class MainViewTests(TestCase):
	def testMainViewShowsUserInfo(self):
		self.client.login(username='sahsko', password='poland')
		response = self.client.get(reverse('main'))
		self.assertContains(response,"Name: Olexnadr Surname: Lykhenko")
