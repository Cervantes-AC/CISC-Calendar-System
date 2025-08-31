from django.urls import path
from . import views

app_name = 'calendar'

urlpatterns = [
    path('', views.calendar_home, name='calendar_home'),

    # Org Officer
    path('add/', views.add_event, name='add_event'),
    path('manage/', views.manage_calendar, name='manage_calendar'),

    # Admin
    path('approval/', views.approval, name='approval'),
    path('update-status/<int:event_id>/<str:status>/', views.update_event_status, name='update_event_status'),
    path('admin-calendar/', views.admin_calendar, name='admin_calendar'),

    # Students/Faculty
    path('view/', views.view_events, name='view_events'),

    # JSON endpoint
    path('events-json/', views.events_json, name='events_json'),
]
