"""
URL configuration for Projects_System_for_Managers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landig_and_dashborad.urls'), name= 'home'),
    path('signup/', include('signup.urls'),name= 'signup'),
    path('signin/', include('sign_in.urls'),name= 'signin'),
    path('projects_task_activities/', include('projects_tasks_and_activities.urls'),name= 'projects_task_activities'),
    path('team/', include('user_work_space_manager.urls'),name= 'team')
]
