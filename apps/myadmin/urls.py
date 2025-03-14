from django.urls import path
from . import views 

urlpatterns = [

    path('dashboard/', views.dashboard_admin, name='dashboard-admin'),  # Tambahkan pola URL untuk dashboard-admin
    path('manage-users/', views.manage_users, name='manage-users'),  # Tambahkan pola URL untuk manage-users
    path("change-user-role/", views.change_user_role, name="change_user_role"),
    path('log-activity/', views.log_activity, name='log-activity'),  # Tambahkan pola URL untuk log-activity
    path('profile/', views.profile_admin, name='profile-admin'),  # Tambahkan pola URL untuk profile-admin
    path("update-profile/<int:user_id>/", views.update_profile, name="update_profile"),
    path('change-password/', views.change_password, name='change-password'),

]