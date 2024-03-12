
    
from django.test import Client, RequestFactory
from django.urls import reverse
import pytest
from django.shortcuts import render
from django.contrib.auth.models import User
from django.test import RequestFactory
from pytest_django.asserts import assertTemplateUsed
from django.test import TestCase

from profiles.models import Profile




class ProfilesViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username="username", password="password")
        Profile.objects.create(user=user, favorite_city="favorite")
        
    @pytest.mark.django_db
    def test_index_view(self):

        uri = 'profiles:index'
        path = reverse(uri)

        client = Client()
        response = client.get(path)
        content = response.content.decode()

        assert '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")
    
    @pytest.mark.django_db
    def test_letting_view(self):
        uri = 'profiles:profile'
        path = reverse(uri, kwargs={'username': "username"})
        client = Client()
        response = client.get(path)
        content = response.content.decode()

        assert '<title>username</title>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")
    
