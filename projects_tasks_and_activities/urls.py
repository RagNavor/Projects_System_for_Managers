from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.projects,name='projects'),
    path('create_project/', views.create_project,name='create_project'),
    path('delete_project/<int:id>', views.delete_project,name='delete_project'),
    path('update_project/<int:id>', views.update_project,name='update_project'),
    path('tasks/', views.tasks,name='tasks'),
    path('create_task/', views.create_tasks,name='create_task'),
    path('detail_task/<int:id>', views.detail_task,name='detail_task'),
    path('delete_task/<int:id>', views.delete_task,name='delete_task'),
    path('update_task/<int:id>', views.update_task,name='update_task'),
    path('create_activity/<int:id>', views.create_activity,name='create_activity'),
    path('update_activity/<int:id>', views.update_task,name='update_task'),
    
    
]