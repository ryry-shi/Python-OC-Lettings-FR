"""
    module for register profiles app models too django administration panels
"""
from django.contrib import admin

from profiles.models import Profile

admin.site.register(Profile)
