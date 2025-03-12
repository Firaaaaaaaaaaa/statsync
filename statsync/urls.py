"""
URL configuration for statsync project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
# from django.urls import path, include
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Tambahkan impor ini



urlpatterns = [
    # path('django-admin/', admin.site.urls),  # Admin bawaan Django
    # path('auth/', include('apps.auth.urls')),  # Authentication
    # path('', include('apps.user.urls')),  # User URLs
    # path('admin/', include('apps.admin.urls')),  # Admin Dashboard
    # path('admin_sidebar/', include('apps.admin.urls')),
    
    # path('admin/', admin.site.urls),  
    # path('auth/', include('apps.auth.urls')),
    # path('', include('apps.user.urls')), 
    
    #path('admin/', admin.site.urls),  # Django's built-in admin panel
    #path('admin_sidebar', include('apps.admin.urls')),  

    path('admin/', admin.site.urls),  # Django's built-in admin panel
    path('adm/', include('apps.myadmin.urls')),  # Admin Dashboard URLs
    # path('login/', auth_views.LoginView.as_view(), name='login'),  # Tambahkan pola URL untuk login
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Tambahkan pola URL untuk logout
    path('', include('apps.myauth.urls')),  # User URLs
    path('user/', include('apps.myuser.urls')),  # User URLs
    #path('auth/', include('apps.myauth.urls')),  # Authentication URLs
]