from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.test import TestCase


class ProfilesViewTest(TestCase):

    @pytest.mark.django_db
    def test_index_view(self):

        uri = 'index'
        path = reverse(uri)

        client = Client()
        response = client.get(path)
        content = response.content.decode()

        assert '''<h1 class="page-header-ui-title mb-3 display-6">
            Welcome to Holiday Homes</h1>''' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "index.html")
