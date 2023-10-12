from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create_user/', views.create_user,name='create user'),
    path('create_work_space/',views.create_work_space, name='create work space'),
    
]