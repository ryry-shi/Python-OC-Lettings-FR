"""
    Module for oc_lettings_site views testing
"""

from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.test import TestCase


class ViewTest(TestCase):
    """
        Class for testing oc_lettings_site views
    """
    @pytest.mark.django_db
    def test_index_view(self):
        """
            Test of index view
        """
        # GIVEN - path to index
        uri = 'index'
        path = reverse(uri)

        # WHEN - making get request to path
        client = Client()
        response = client.get(path)
        content = response.content.decode()

        # WHAT - look for valid title and valid response status
        assert 'Welcome to Holiday Homes</h1>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")
