"""
    module for register lettings app models too django administration panels
"""
from django.contrib import admin

from lettings.models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)
