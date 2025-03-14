from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from apps.myauth.models import CustomUser, Role
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash


@login_required
def manage_users(request):
    users = CustomUser.objects.select_related('id_role').all()  # Ambil data user beserta role-nya
    roles = Role.objects.all()  # Ambil daftar semua role
    return render(request, "admin/manage-users.html", {"users": users, "roles": roles})  # Kirim data roles ke template

@login_required
def change_user_role(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        new_role_id = request.POST.get("role_id")

        user = get_object_or_404(CustomUser, id=user_id)
        new_role = get_object_or_404(Role, id_role=new_role_id)

        user.id_role = new_role
        user.save()

        return JsonResponse({"success": True, "new_role": new_role.nama_role})

    return JsonResponse({"success": False, "error": "Invalid request"})

@login_required
def dashboard_admin(request):
    return render(request, 'admin/dashboard-admin.html')

@login_required
def log_activity(request):
    return render(request, 'admin/log-activity.html')

User = get_user_model()

@login_required
def profile_admin(request):
    return render(request, 'common/profile-admin.html')

@login_required
def profile_view(request):
    user = request.user  

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()  # Ambil full name dari form
        username = request.POST.get("username", "").strip()

        if not full_name:
            messages.error(request, "Full name cannot be empty.")
            return redirect("profile-admin")

        if not username:
            messages.error(request, "Username cannot be empty.")
            return redirect("profile-admin")

        if User.objects.filter(username=username).exclude(id=user.id).exists():
            messages.error(request, "Username is already taken.")
            return redirect("profile-admin")

        # Simpan full name langsung ke first_name
        user.first_name = full_name  
        user.username = username
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile-admin")  

    return render(request, "common/profile-admin.html", {"user": user})

@login_required
def update_profile(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        full_name = request.POST.get("fullName", "").strip()
        username = request.POST.get("username", "").strip()

        if full_name:
            user.first_name = full_name
        if username:
            user.username = username

        user.save()
        return redirect(request.path)  # Redirect ke halaman yang sama setelah update

    return render(request, "common/profile-admin.html", {"user": user})

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('password')
        new_password = request.POST.get('newpassword')
        renew_password = request.POST.get('renewpassword')

        user = request.user

        # Cek apakah current password benar
        if user.check_password(current_password) and new_password == renew_password:
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Agar tetap login
        return redirect('profile-admin')  # Kembali ke halaman profil

    return redirect('profile-admin')