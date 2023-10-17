from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from user_work_space_manager.models import RolAssignment,UserProfile,WorkSpaces
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'sign_in.html')
    if request.method == 'POST':
        user_login = authenticate(request=request,username=request.POST['name'],password =request.POST['password1'])
        if user_login is not None:
            user_login= UserProfile.objects.get(username = request.POST['name'])
            login(request=request,user=user_login)
            return redirect('select work space',)
        return HttpResponse('Usuario no authenticado')


def select_work_space(request):
    if request.method == 'GET':
        list_test = RolAssignment.objects.filter(user = request.user.pk)
        list_work_space= []
        for i in list_test:
            #ws= WorkSpaces.objects.get(pk = i.work_space)
            list_work_space.append(i.work_space)
        print(list_work_space)
        return render(request, 'select_work_space.html',{
            'works_spaces': list_work_space
        })
        
def close_session(request):
    logout(request)
    return redirect('landing')