from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.
def loginas(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']

        u = login.objects.filter(Q(user_name=user_name) & Q(password=password))
        if u.count() > 0:
            request.session['id'] = u[0].user_id
            if u[0].user_type == 0:
                return redirect('http://127.0.0.1:8000/')
    return render(request, 'home/home.html')
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        #file_upload1 = request.POST.get('file_upload1')
        photo = request.FILES.get('photo_upload')
        confirm = request.POST.get('confirm')
        user_name = request.POST.get('user_name')
        r = registration(name=name, email=email, address=address, phone=phone, photo=photo)
        r.save()
        l = login(user_name=user_name, password=confirm, user_type='SW', user_id=r.user_id)
        l.save()

        return redirect("http://127.0.0.1:8000/login/")


    return render(request, 'home/registration.html')
def home(request):
    return render(request, 'home/home.html')
