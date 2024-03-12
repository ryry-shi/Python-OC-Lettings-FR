from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
from django.test import TestCase

from lettings.models import Letting, Address


class LettingViewTest(TestCase):

    def setUp(self):
        # Créer les objets nécessaires pour le test
        address = Address.objects.create(
            number=8,
            street="rue",
            city="stchamand",
            state="avignon",
            zip_code="84000",
            country_iso_code="country"
        )
        Letting.objects.create(title='Big', address=address)

    @pytest.mark.django_db
    def test_index_view(self):

        uri = 'lettings:index'
        path = reverse(uri)

        client = Client()
        response = client.get(path)
        content = response.content.decode()

        assert '<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/index.html")

    @pytest.mark.django_db
    def test_letting_view(self):
        uri = 'lettings:letting'
        path = reverse(uri, kwargs={'letting_id': 1})
        client = Client()
        response = client.get(path)
        content = response.content.decode()

        assert '<title>Big</title>' in content
        assert response.status_code == 200
        assertTemplateUsed(response, "lettings/letting.html")
