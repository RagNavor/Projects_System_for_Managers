from django.contrib import admin
from.models import Project,Tasks,Activities,CommentsActivities,CommentsProject,CommentsTasks

# Register your models here.
admin.site.register(Project)
admin.site.register(Tasks)
admin.site.register(Activities)
admin.site.register(CommentsActivities)
admin.site.register(CommentsProject)
admin.site.register(CommentsTasks)