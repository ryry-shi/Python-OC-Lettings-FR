"""
    models module for profiles application
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """
        A class to represent a user profile
    """
    class Meta:
        db_table = 'oc_lettings_site_profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
