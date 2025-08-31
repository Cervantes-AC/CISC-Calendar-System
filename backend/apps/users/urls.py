from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards
    path('dashboard/', views.dashboard_view, name='dashboard_view'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/faculty/', views.faculty_dashboard, name='faculty_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/orgofficer/', views.orgofficer_dashboard, name='orgofficer_dashboard'),

    # Profile
    path('profile/', views.profile_view, name='profile'),

    # Manage Users (Admin only)
    path('manage-users/', views.manage_users, name='manage_users'),
]
