from django.urls import path
from . import views

urlpatterns = [
    path('',views.team,name= 'team'),
    path('create_user/', views.create_user_in_workspace,name='create_user'),
    path('assign_leader/', views.assign_leader, name='assign_leader')
]