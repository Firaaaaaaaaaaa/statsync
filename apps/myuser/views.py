
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from apps.myauth.models import CustomUser, Role
import json
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import update_session_auth_hash

@login_required
def dashboard_user(request):
    return render(request, 'user/dashboard-user.html')

@login_required
def brstoexcel(request):
    return render(request, 'user/brs-to-excel.html')

@login_required
def rekapitulasi(request):
    return render(request, 'user/rekapitulasi.html')

@login_required
def rekapitulasi_keseluruhan(request):
    return render(request, 'user/rekapitulasi-keseluruhan.html')

@login_required
def rekapitulasi_pribadi(request):
    return render(request, 'user/rekapitulasi-pribadi.html')

@login_required
def profile_user(request):
    return render(request, 'common/profile-user.html')


@login_required
def profile_view(request):
    user = request.user  

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()  # Ambil full name dari form
        username = request.POST.get("username", "").strip()

        if not full_name:
            messages.error(request, "Full name cannot be empty.")
            return redirect("profile-user")

        if not username:
            messages.error(request, "Username cannot be empty.")
            return redirect("profile-user")

        if User.objects.filter(username=username).exclude(id=user.id).exists():
            messages.error(request, "Username is already taken.")
            return redirect("profile-user")

        # Simpan full name langsung ke first_name
        user.first_name = full_name  
        user.username = username
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect("profile-user")  

    return render(request, "common/profile-user.html", {"user": user})

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

    return render(request, "common/profile-user.html", {"user": user})

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
        return redirect('profile-user')  # Kembali ke halaman profil

    return redirect('profile-user')