from django.shortcuts import render

def dashboard_admin(request):
    return render(request, 'admin/dashboard-admin.html')

def manage_users(request):
    return render(request, 'admin/manage-users.html')

def log_activity(request):
    return render(request, 'admin/log-activity.html')

def profile_admin(request):
    return render(request, 'common/profile-admin.html')
