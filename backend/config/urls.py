from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('calendar/', include('apps.calendar_app.urls')),
    path('', RedirectView.as_view(url='/users/login/')),  # <-- root URL redirects to login page
]
# This file defines the URL patterns for the Django project, including admin, user management, and calendar app URLs.
# The root URL redirects to the login page for user convenience.    