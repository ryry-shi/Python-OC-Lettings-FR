"""
    views module for oc_lettings_site application
"""

from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque
# iaculis enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    return render(request, 'index.html')


def page_not_found_view(request, *args, **kwargs):
    return render(request, '404.html', status=404)


def server_error_view(request, *args, **kwargs):
    return render(request, '500.html', status=500)
