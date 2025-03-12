from django.urls import path
from . import views  # Import the views module from the current package

urlpatterns = [
    path('dashboard/', views.dashboard_admin, name='dashboard-admin'),  # Tambahkan pola URL untuk dashboard-admin
    path('manage-users/', views.manage_users, name='manage-users'),  # Tambahkan pola URL untuk manage-users
    path('log-activity/', views.log_activity, name='log-activity'),  # Tambahkan pola URL untuk log-activity
    path('profile/', views.profile_admin, name='profile-admin'),  # Tambahkan pola URL untuk profile-admin
]