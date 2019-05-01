from django.test import Client,TestCase
from django.contrib.auth.models import User
from homepage.models import UserProfileInfo
from .models import *
from homepage.forms import *
class TestingHomepage(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
        self.client=None
        self.request_url='/homepage/register/'
    def test_register(self):
        self.client=Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)


    def test_uploadby_authenticated_user_id(self):
      self.client=Client()
      self.client.force_login(self.createadmin)
      response = self.client.get('homepage/randomm')
      self.assertEqual(response.status_code, 404)

# Create your tests here.
class TestingHomepage2(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
        self.client=None
        self.request_url='/homepage/user_login/'
    def test_register(self):
        self.client=Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)


    def test_uploadby_authenticated_user_id(self):
      self.client=Client()
      self.client.force_login(self.createadmin)
      response = self.client.get('homepage/randomm')
      self.assertEqual(response.status_code, 404)
class TestingHomepage3(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
        self.client=None
        self.request_url='/homepage/feedback/'
    def test_register(self):
        self.client=Client()
        response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)


    def test_uploadby_authenticated_user_id(self):
      self.client=Client()

      response = self.client.get('homepage/randomm')
      self.assertEqual(response.status_code, 404)
class User_Form_Test(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
    # Valid Form Data
    def test_UserForm_valid(self):
        form = UserForm(data={'email': "user@mp.com", 'password': "user1234", 'first_name': "user",'last_name':"testuser",'username':"testuser",'re_password':"user1234"})
        self.assertTrue(form.is_valid())
class FeedBack_Form_Test(TestCase):
    def setUp(self):
        self.createadmin=User.objects.create_user(username="test user",email="test@gmail.com",password="test password")
    # Valid Form Data
    def test_FeedBAckForm_valid(self):
        form = FeedbackForm(data={'name': "user", 'rating': "5", 'text':"my picture"})
        self.assertTrue(form.is_valid())
