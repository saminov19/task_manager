import json
from django.test import TestCase, Client, RequestFactory
from rest_framework import status
from tasks.models import User
from django.http import HttpRequest
from rest_framework.test import APITestCase
from authentication.serializers import UserRegistrationSerializer, UserLoginSerializer
from .views import CustomObtainJSONWebToken

class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.registration_url = '/api/auth/register/'

    def test_successful_registration(self):
        data = {
            'email': 'testuser@gmail.com',
            'password': 'securepassword',
            'password2': 'securepassword'
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_with_existing_username(self):
        User.objects.create_user(email='testuser@gmail.com', password='password')
        data = {
            'email': 'testuser@gmail.com',
            'password': 'securepassword',
            'password2': 'securepassword'
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_missing_data(self):
        data = {
            'password': 'securepassword',
            'password2': 'securepassword'
        }
        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




class LoginViewTest(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.login_url = '/api/auth/login/'

    def test_login_with_invalid_credentials(self):
        request = self.factory.post(self.login_url, {'email': 'invalid@example.com', 'password': 'wrongpassword'})
        response = CustomObtainJSONWebToken.as_view()(request)
        self.assertEqual(response.status_code, 400)  

    def test_successful_login(self):
        user = User.objects.create_user(email='user@example.com', password='password')
        request = self.factory.post(self.login_url, {'email': 'user@example.com', 'password': 'password'})
        response = CustomObtainJSONWebToken.as_view()(request)
        self.assertEqual(response.status_code, 200)



class UserRegistrationSerializerTest(TestCase):
    def test_valid_user_registration_data(self):
        data = {
            'email': 'testuser@gmail.com',
            'password': 'securepassword',
            'password2': 'securepassword'
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.email, 'testuser@gmail.com')




class UserLoginSerializerTest(TestCase):
    def test_valid_user_login_data(self):
        user = User.objects.create_user(email='user@example.com', password='password')
        
        data = {'email': 'user@example.com', 'password': 'password'}
        serializer = UserLoginSerializer(data=data)
        
        self.assertTrue(serializer.is_valid())
