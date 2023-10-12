from django.contrib import admin
from .models import User, UserProfile,WorkSpaces,RolAssignment

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(WorkSpaces)
admin.site.register(RolAssignment)