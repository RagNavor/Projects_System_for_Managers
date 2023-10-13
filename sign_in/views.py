from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from user_work_space_manager.models import RolAssignment,UserProfile
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'sign_in.html')
    if request.method == 'POST':
        user_login = authenticate(request=request,username=request.POST['name'],password =request.POST['password1'])
        if user_login is not None:
            user_login= UserProfile.objects.get(username = request.POST['name'])
            login(request=request,user=user_login)
            return redirect('select work space')
        return HttpResponse('Usuario no authenticado')


def select_work_space(request,id):
    if request.method == 'GET':
        user = UserProfile.objects.get(pk = id)
        return render(request, 'select_work_space.html')