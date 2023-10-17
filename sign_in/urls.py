from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='signin'),
    path('select_work_space/',views.select_work_space ,name= 'select work space'),
    path('logout',views.close_session,name= 'close_session')
]
