"""
    A module for routing to oc_lettings_views application views
"""

from django.contrib import admin
from django.urls import path, include

from . import views


handler404 = views.page_not_found_view
handler500 = views.server_error_view


def trigger_error(request):
    division_by_zero = 1 / 0 # noqa


urlpatterns = [
    path('', views.index, name='index'),
    path('profiles/', include('profiles.urls')),
    path('lettings/', include('lettings.urls')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
]
