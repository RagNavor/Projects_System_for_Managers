from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='signin'),
    path('select_work_space/id',views.select_work_space ,name= 'select work space')
]
