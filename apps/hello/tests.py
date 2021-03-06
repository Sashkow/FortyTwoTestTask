"""tests"""
from django.test import TestCase

from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User

from django.test.client import RequestFactory
from django.conf import settings
from apps.hello.models import RequestInfo, UserProfile
from apps.hello.middleware import RequestsToDataBase

from django.conf import settings
from django.utils.functional import LazyObject

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


class RequestsToDataBaseTestsMoreThanTenRecords(TestCase):
    fixtures = ['middleware_testing_data_15_records.json']

    def testRequestsToDataBaseExists(self):
        self.assertEquals('MIDDLEWARE_CLASSES' in dir(settings), True)
        self.assertEquals('apps.hello.middleware.RequestsToDataBase' \
         in settings.MIDDLEWARE_CLASSES, True)

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
        request = self.factory.get(reverse('main'))
        rtb = RequestsToDataBase()
        rtb.process_request(request)
        requestToDB = pickle.dumps(request.REQUEST)

        ri = RequestInfo.objects.latest('pub_date')
        requestFromDB = ri.pickled_request

        self.assertEquals(requestToDB, requestFromDB)

    def testExistsShowFirstRequests(self):
        c = Client()
        response = c.get(reverse('show-first-requests'))
        self.assertEquals(response.status_code, 200)

    def testShowFirstRequestsViewsDataCorrectly(self):
        c = Client()
        response = c.get(reverse('show-first-requests'))
        self.assertContains(response, "1. 2014-12-22 16:19:56")
        self.assertEquals( \
            str(response).count('<p class="request_record">'), 10)


class RequestsToDataBaseTestsLessThanTenRecords(TestCase):
    fixtures = ['middleware_testing_data_5_records.json']

    def testShowFirstRequestsViewsDataCorrectlyLessThanTenRecords(self):
        c = Client()
        response = c.get(reverse('show-first-requests'))    
        self.assertContains(response, "1. 2014-12-23 11:52:17")
        #more records added while getting response, so 7, not 5
        self.assertEquals( \
            str(response).count('<p class="request_record">'), 7) 


class ContextProcessorTests(TestCase):
    def testContextProcessorRuns(self):
        c = Client()
        response = c.get(reverse('show-django-settings'))    
        self.assertEquals('django_settings' in response.context, True)
        self.assertEquals(type(response.context['django_settings']), \
            type(settings))


class EditFormTests(TestCase):
    fixtures = ['hello_main_view_testdata.json']

    def testEditUserInfoResponds(self):
        c = Client()
        response = c.get(reverse('edit-user-info'))
        self.assertEquals(response.status_code, 200)

    def testEditUserInfoContainsContextData(self):
        c = Client()
        c.login(username='admin', password='admin')
        response = c.get(reverse('show-django-settings'))    
        self.assertEquals('user' in response.context, True)
        u = User()
        self.assertEquals(isinstance(response.context['user'],LazyObject),True)
        