from django.urls import path
from . import views  # make sure views.py is in the same folder

app_name = 'calendar_app'

urlpatterns = [
    path('', views.home_view, name='home'),
]
