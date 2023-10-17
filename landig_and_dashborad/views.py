from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_work_space_manager import models as user_workspace
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser

# Create your views here.
def index(request):
    anonimo = AnonymousUser()
    if request.user.pk == None and request.user == anonimo:        
        return render(request,'landing.html')
    print(request.user)
    return redirect('home')

@login_required
def dashboard(request):
    if request.method == 'GET':
        return redirect('select work space')
    test = request.POST
    print(test)
    work_space = user_workspace.WorkSpaces.objects.get(pk=request.POST['work_space'])
    request.session['selected_workspace'] = work_space.pk   
    team= [ {user.user, user.rol} for user in user_workspace.RolAssignment.objects.filter(work_space=work_space.pk)]
    Projects=[]
    Tasks=[]
    Activities=[]
    
    return render(request,'dashboard.html',{
        'work_space': work_space,
        'team':team
    })