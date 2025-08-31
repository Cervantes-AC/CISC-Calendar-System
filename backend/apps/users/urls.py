from django.urls import path
from . import views

app_name = 'users'  # <-- add this line

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
# This file defines the URL patterns for user-related views such as registration, login, and logout.    