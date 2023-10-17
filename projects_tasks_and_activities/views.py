from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_work_space_manager.models import UserProfile, WorkSpaces, RolAssignment
from .models import Project, Tasks
from datetime import datetime

# Create your views here.
@login_required
def projects(request):
    now = str(datetime.now())
    
    if request.method == 'GET':
        workspace = WorkSpaces.objects.get(pk= request.session['selected_workspace'])
        projects = Project.objects.filter(created_by_user = request.user.pk, in_work_space = workspace) 
        return render(request,'projects_resume.html',{
            'work_space':  workspace,
            'now':now,
            'projects':projects
        })
        
@login_required
def create_project(request):
    workspace = WorkSpaces.objects.get(pk= request.session['selected_workspace'])
    user= UserProfile.objects.get(pk=request.user.pk)
    new_project = Project.objects.create(
        created_by_user=user,
        in_work_space= workspace,
        description = request.POST['description'],
        name=request.POST['name'],
        dead_line = request.POST['dead_line']
    )
    
    return redirect('projects')

def delete_project(request,id):
    Project.objects.get(pk=id).delete()
    return redirect('projects')

def update_project(request,id):
    project= Project.objects.get(pk=id)
    if request.method == 'GET':
        
        return render(request,'project_update.html',{
             'project':project 
            })
    else:
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.save()
        return redirect('projects')

@login_required
def tasks(request):
    if request.method == 'GET':
        now = str(datetime.now())
        workspace = WorkSpaces.objects.get(pk= request.session['selected_workspace'])
        projects = Project.objects.filter(created_by_user = request.user.pk, in_work_space = workspace)
        task_group_by_projects:list=[]
        for project in projects:
            tasks_group = Tasks.objects.filter(belongs_project = project.pk)
            task_group_by_projects.append((project,tasks_group))
            
        return render(request,'tasks_resume.html',{
            'now':now,
            'workspace':workspace,
            'projects':projects,
            'task_group_by_projects':task_group_by_projects
        })

def create_tasks(request):
    user = UserProfile.objects.get(pk=request.user.pk)
    work_space= WorkSpaces.objects.get(pk=request.session['selected_workspace'])
    project = Project.objects.get(pk=request.POST['projects'])
    new_task = Tasks.objects.create(
        created_by_user=user,
        belongs_project=project,
        in_work_space=work_space,
        name=request.POST['name'],
        description=request.POST['description'],
        dead_line=request.POST['dead_line']
    )
    new_task.save()
    return redirect('tasks')

def delete_task(request,id):
    task = Tasks.objects.get(pk=id).delete()
    return redirect('tasks')

def update_task(request,id):
    task = Tasks.objects.get(pk = id)
    if request.method == 'GET':
        return render(request,'task_update.html',{
            'task':task
        })
    task.name =request.POST['name']
    task.description = request.POST['description']
    task.save()
    return redirect('tasks')
    