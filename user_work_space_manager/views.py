from django.shortcuts import render,redirect
from .models import WorkSpaces, UserProfile,RolAssignment,Teams

# Create your views here.

def team(request):
    work_space = WorkSpaces.objects.get(pk= request.session['selected_workspace'])
    area_leads = RolAssignment.objects.filter(work_space= work_space,rol= 'AREA_LEAD')
    teams = []
    for lead in area_leads:
        colaborators = Teams.objects.filter(area_lead=lead.user)
        teams.append((lead,colaborators))
    collaborators_without_area_lead = Teams.objects.filter(area_lead__isnull=True)
    print(collaborators_without_area_lead)
    print(area_leads)
    return render(request,'team.html',{
        'teams':teams,
        'collaborators_without_area_lead':collaborators_without_area_lead
    })
    
def create_user_in_workspace(request):
    work_space = WorkSpaces.objects.get(pk= request.session['selected_workspace'])
    new_user=UserProfile.objects.create_user(
            username= request.POST['name'],
            email=request.POST['email'],
            password=request.POST['password1']
        )
    rol = RolAssignment.objects.create(
        user = new_user,
        work_space =work_space,
        rol = request.POST['rol']
    )
    if request.POST['rol'] == 'AREA_LEAD':
        team =Teams.objects.create(
            area_lead=new_user,
            work_space =work_space
        )
    elif request.POST['rol'] == 'COLLABORATOR':
        team =Teams.objects.create(
            collaborator=new_user,
            work_space =work_space
        )
    return redirect('team')

def assign_leader(request):
    print(request.POST['lead'])
    area_lead = UserProfile.objects.get(pk=request.POST['lead'])
    colaborators = UserProfile.objects.get(username=request.POST['collaborator'])
    new_assingnement = Teams.objects.get(
        collaborator = colaborators,
        area_lead__isnull=True
    )
    new_assingnement.area_lead=area_lead
    new_assingnement.save()
    
    return redirect('team')



