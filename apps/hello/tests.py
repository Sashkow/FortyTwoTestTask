from django.test import TestCase

from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User

from django.test.client import RequestFactory
from django.conf import settings
from models import RequestInfo
from middleware import RequestsToDataBase


import pickle
# Create your tests here.

class MainViewTests(TestCase):
    fixtures = ['hello_main_view_testdata.json']

    def testUserHasNeededProfileAttributes(self):
        u = User.objects.get(username='admin')
        self.assertEquals(hasattr(u, 'userprofile'), True)
        self.assertEquals(hasattr(u.userprofile, 'bio'), True)
        self.assertEquals(hasattr(u.userprofile, 'jabber'), True)
        self.assertEquals(hasattr(u.userprofile, 'skype'), True)
        self.assertEquals(hasattr(u.userprofile, 'other_contacts'), True)
        self.assertEquals(hasattr(u.userprofile, 'birth_date'), True)

    def testMainViewShowsUserInfo(self):
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(reverse('main'))
        self.assertContains(response, "Name: Lykhenko")
        self.assertContains(response, "Last name: Olexandr")
        self.assertContains(response, "Date of birth: Jan. 2, 1991")
        self.assertContains(response, "Bio:")
        self.assertContains(response, "Lorem ipsum")
        self.assertContains(response, "Jabber: sashko@jabber")
        self.assertContains(response, "Skype: someSkypeId")
        self.assertContains(response, "Other contacts:")
        self.assertContains(response, "facebook.com")

class RequestsToDataBaseTests(TestCase):
    def testRequestsToDataBaseExists(self):
        self.assertEquals('MIDDLEWARE_CLASSES' in dir(settings), True)
        self.assertEquals('apps.hello.middleware.RequestsToDataBase' \
         in settings.MIDDLEWARE_CLASSES,True)

    def testRequestInfoModelUpdates(self):
        #count objects in RequestInfo model
        #simulate request to root page
        #count objects in RequestInfo model
        #check if amount increased by one
        initialObjectsCount = int(RequestInfo.objects.count())
        c = Client()
        c.get(reverse('main'))
        newObjectsCount = int(RequestInfo.objects.count())
        self.assertEquals(newObjectsCount - initialObjectsCount, 1)

    def setUp(self):
        self.factory = RequestFactory()

    def testRequestInfoModelUpdatesWithCorrectData(self):
        c = Client()
        request = self.factory.get(reverse('main'))
        rtb = RequestsToDataBase()
        rtb.process_request(request)
        requestToDB = pickle.dumps(request.REQUEST)
        
        ri = RequestInfo.objects.latest('pub_date')
        requestFromDB = ri.pickled_request

        self.assertEquals(requestToDB, requestFromDB)        