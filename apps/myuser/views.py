from django.shortcuts import render

def dashboard_user(request):
    return render(request, 'user/dashboard-user.html')

def brstoexcel(request):
    return render(request, 'user/brs-to-excel.html')

def rekapitulasi(request):
    return render(request, 'user/rekapitulasi.html')

def rekapitulasi_keseluruhan(request):
    return render(request, 'user/rekapitulasi-keseluruhan.html')

def rekapitulasi_pribadi(request):
    return render(request, 'user/rekapitulasi-pribadi.html')

def profile_user(request):
    return render(request, 'common/profile-user.html')
