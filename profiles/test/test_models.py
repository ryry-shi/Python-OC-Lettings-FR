"""
    Module for profiles models testing
"""
from django.test import TestCase
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):
    """
        Class for testing profile model
    """
    @classmethod
    def setUpTestData(cls):
        """
            Set up non-modified objects used by all test methods
        """
        user = User.objects.create(username="useaaaaaaaaaaarname", password="password")
        Profile.objects.create(user=user, favorite_city="favorite")

    def test_user_label(self):
        """
            Test of Profiles.user attribute's label
        """
        field_label = Profile._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_user_value(self):
        """
            Test of Profiles.user attribute's value
        """
        profile = Profile.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(profile.user, user)

    def test_user_type(self):
        """
            Test of Profiles.user attribute's type
        """
        user_type = Profile._meta.get_field("user").get_internal_type()
        self.assertEqual(user_type, 'OneToOneField')

    def test_favorite_city_label(self):
        """
            Test of Profiles.favorite_city attribute's label
        """
        field_label = Profile._meta.get_field('favorite_city').verbose_name
        self.assertEqual(field_label, 'favorite city')

    def test_favorite_city_value(self):
        """
            Test of Profiles.favorite_city attribute's value
        """
        profile = Profile.objects.get(id=1)
        self.assertEqual(profile.favorite_city, "favorite")

    def test_favorite_city_type(self):
        """
            Test of Profiles.favorite_city attribute's type
        """
        favorite_city_type = Profile._meta.get_field("favorite_city").get_internal_type()
        self.assertEqual(favorite_city_type, 'CharField')
