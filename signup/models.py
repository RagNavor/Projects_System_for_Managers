from django.db import models
from django.contrib.auth.models import User
from .choices_signup import USER_ROL

# Create your models here.
class WorkSpaces(models.Model):
    name = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name


class RolAssignment(models.Model):
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
    work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE)
    rol = models.CharField( max_length=20, choices=USER_ROL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'El usuario {self.user} tiene el en el work space {self.work_space} tiene el rol de {self.rol}'
    
class Users(User):
    users_work_space = models.OneToOneField(User, on_delete=models.CASCADE, related_name='users_User')
    work_space: models.ManyToManyField(WorkSpaces, through=RolAssignment)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.users_work_space