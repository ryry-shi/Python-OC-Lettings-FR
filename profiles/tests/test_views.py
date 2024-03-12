"""
    Module for profiles views testing
"""
from django.test import Client
from django.urls import reverse
import pytest
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed
from django.test import TestCase

from profiles.models import Profile


class ProfilesViewTest(TestCase):
    """
        Class for testing profiles a views
    """
    @classmethod
    def setUpTestData(cls):
        """
            Set up non-modified objects used by all test methods
        """
        user = User.objects.create(username="username", password="password")
        Profile.objects.create(user=user, favorite_city="favorite")

    @pytest.mark.django_db
    def test_index_view(self):
        """
            test for testing profiles index view
        """
        # GIVEN - path to profiles:index
        uri = 'profiles:index'
        path = reverse(uri)

        # WHEN - making get request to path
        client = Client()
        response = client.get(path)
        content = response.content.decode()

        # WHAT - look for valid title and valid response status
        assert '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/index.html")

    @pytest.mark.django_db
    def test_profile_view(self):
        """
            test for testing profiles:profile view
        """
        # GIVEN - path to profiles:profile
        uri = 'profiles:profile'
        path = reverse(uri, kwargs={'username': "username"})

        # WHEN - making get request to path
        client = Client()
        response = client.get(path)
        content = response.content.decode()

        # WHAT - look for valid title and valid response status
        assert '<title>username</title>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "profiles/profile.html")
