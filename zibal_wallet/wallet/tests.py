import unittest
from django.test import Client
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

class InitCase(TestCase):
    client = Client()

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User(username="danialkamali",password="123456789",email="daniel.kamali@yahoo.com")
    def init_test(self):
        a = InitCase.client.get("/init/")
        self.assertEqual(a.status_code, 200)

    def middleware_test(self):


        a = self.factory.post('/init/', {"date": "1397/2/3", "names": ["ghasem", "ali", "mahdi", "mohammad"]},
                                 content_type="application/json")

        self.assertEqual(a.status_code, 405)

