from django.db import models
from .choices_user_work_spaces import USER_ROL
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
class WorkSpaces(models.Model):
    name = models.CharField( max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name


class RolAssignment(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE)
    rol = models.CharField( max_length=20, choices=USER_ROL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'El usuario {self.user} tiene el en el work space {self.work_space} tiene el rol de {self.rol}'
    
class UserProfile(AbstractUser):
    
    work_space: models.ManyToManyField(WorkSpaces, through=RolAssignment,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.username