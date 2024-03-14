"""
    module used for app configuration
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
        class used for app configuration
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles"
