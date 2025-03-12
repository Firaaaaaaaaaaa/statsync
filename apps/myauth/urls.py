from django.urls import path
from . import views  # Import the views module from the current package

urlpatterns = [
    path('login/', views.user_login, name='login'), 
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'), 
     
]