from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_work_space_manager.models import  WorkSpaces,RolAssignment, UserProfile
from projects_tasks_and_activities.models import Project, Tasks, Activities
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
    user = UserProfile.objects.get(pk =request.user.pk)
    work_space = WorkSpaces.objects.get(pk=request.session['selected_workspace'])
    work_space_change = RolAssignment.objects.filter(user=user)
    team= [ {user.user, user.rol} for user in RolAssignment.objects.filter(work_space=work_space.pk)]
    projects= Project.objects.filter(in_work_space=work_space).filter(in_work_space=work_space)
    tasks= Tasks.objects.select_related('belongs_project').filter(in_work_space=work_space)
    tasks_group_by_project=[]
    
    for project in projects:
        tasks = Tasks.objects.filter(belongs_project=project)
        task_completed = Tasks.objects.filter(belongs_project=project,state='COMPLETED')
        tasks_group_by_project.append((project,tasks,task_completed))
            
    
    
    return render(request,'dashboard.html',{
        'work_space': work_space,
        'team':team,
        'work_space_change':work_space_change,
        'tasks_group_by_project':tasks_group_by_project
    })