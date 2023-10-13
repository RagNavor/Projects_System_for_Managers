from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_work_space_manager.models import User,UserProfile, WorkSpaces, RolAssignment
from django.contrib.auth import authenticate, login

# Create your views here.
#Get
def singup(request):
    return render(request,'signup.html')


#Post
def create_user(request):
    if request.POST['password1'] == request.POST['password2']:
        new_user = UserProfile.objects.create_user(
            username= request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password1']
        )
        login(request,new_user)
        return redirect('create work space')
    
def create_work_space(request):
    print(request.user)
    if request.method == 'GET':
        return render(request,'create_work_space.html',{
        'user':request.user
    })
    if request.method == 'POST':
        new_work_space =WorkSpaces.objects.create(
            name= request.POST['workspace']
        )
        role_assignment = RolAssignment.objects.create(
            user = request.user,
            work_space = new_work_space,
            rol = 'CREATOR_WORK_SPACE'
        )
        return HttpResponse(f'Se creo con exito  {new_work_space} {role_assignment}')