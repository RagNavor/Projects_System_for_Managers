from django.db import models
from signup.models import Users, WorkSpaces
from .choices_projects_task_and_activities import STATE

# Create your models here.
class Project(models.Model):
    created_by_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Project_Users')
    in_work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE,related_name='Project_WorkSpaces')
    state = models.CharField(max_length=15, choices=STATE, default= 'STAND_BY')
    name = models.CharField(max_length=100)
    dead_line = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    
class CommentsProject(models.Model):
    created_by_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='CommentsProject_Users')
    in_work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE,related_name='CommentsProject_WorkSpaces')
    belongs_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='CommentsProject_Project')
    comment = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.comment
    
class Tasks(models.Model):
    created_by_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Tasks_Users')
    belongs_project = models.ForeignKey(Project, on_delete= models.CASCADE, related_name='Tasks_Project')
    in_work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE,related_name='Tasks_WorkSpaces')
    state = models.CharField(max_length=15, choices=STATE, default= 'STAND_BY')
    name = models.CharField(max_length=100)
    dead_line = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    
class CommentsTasks(models.Model):
    created_by_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='CommentsTasks_Users')
    in_work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE,related_name='CommentsTasks_WorkSpaces')
    belongs_Tasks = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='CommentsTasks_Project')
    comment = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.comment
    
class Activities(models.Model):
    created_by_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='Activities_Users')
    belongs_task = models.ForeignKey(Tasks, on_delete= models.CASCADE, related_name='Activities_Task')
    in_work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE,related_name='Activities_WorkSpaces')
    state = models.CharField(max_length=15, choices=STATE, default= 'STAND_BY')
    name = models.CharField(max_length=100)
    dead_line = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    
class CommentsActivities(models.Model):
    created_by_user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='CommentsActivities_Users')
    in_work_space = models.ForeignKey(WorkSpaces, on_delete=models.CASCADE,related_name='CommentsActivities_WorkSpaces')
    belongs_activitie= models.ForeignKey(Project, on_delete=models.CASCADE, related_name='CommentsActivities_Project')
    comment = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.comment