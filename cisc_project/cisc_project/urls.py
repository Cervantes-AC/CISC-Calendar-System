from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", lambda request: redirect("login")),  # 👈 redirect / to login
]
# This file defines the URL patterns for the Django project, including the admin interface and the accounts app.
# The root URL redirects to the login page, ensuring that users are directed to the authentication flow     