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
            return redirect('select work space')
        else:
            return render(request,'sign_in.html',{
                'error':'Usuario o contraseña invalido'
            })


def select_work_space(request):
    if request.method == 'GET':
        user_workspace_relationship = RolAssignment.objects.filter(user = request.user.pk)
        list_work_space= []
        for i in user_workspace_relationship:
            #ws= WorkSpaces.objects.get(pk = i.work_space)
            list_work_space.append(i.work_space)
        work_space_selected=False
        print(list_work_space)
        return render(request, 'select_work_space.html',{
            'works_spaces': list_work_space,
            'work_space_selected':work_space_selected
            
        })
    work_space = WorkSpaces.objects.get(pk=request.POST['work_space'])
    role = RolAssignment.objects.get(user = request.user.pk, work_space=work_space)
    
    request.session['selected_workspace'] = work_space.pk
    request.session['user_rol'] = role.rol
    
    return redirect('home')
        
def close_session(request):
    logout(request)
    return redirect('landing')