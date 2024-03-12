from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(username="username", password="password")
        Profile.objects.create(user=user, favorite_city="favorite")

    def test_user_label(self):
        field_label = Profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_user_value(self):
        profile = Profile.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(profile.user, user)

    def test_number_type(self):
        user_type = Profile._meta.get_field("user").get_internal_type()
        self.assertEqual(user_type, 'OneToOneField')

    def test_favorite_city_label(self):
        field_label = Profile._meta.get_field('favorite_city').verbose_name
        self.assertEqual(field_label, 'favorite city')

    def test_favorite_city_value(self):
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.favorite_city, "favorite")

    def test_favorite_city_type(self):
        favorite_city_type = Profile._meta.get_field("favorite_city").get_internal_type()
        self.assertEqual(favorite_city_type, 'CharField')
