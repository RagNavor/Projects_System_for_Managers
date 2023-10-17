from django.test import TestCase
from user_work_space_manager.models import UserProfile, WorkSpaces,RolAssignment
from .models import Project
# Create your tests here.

class Test_CreateProject(TestCase):
    def create_projects_by_work_space_creator(self):
        '''
        Create user, work space, assign rol  'CREATOR_WORK_SPACE' and create 2 Projects
        '''
        self.new_user= UserProfile.objects.create_user(
            username='Test User',
            email= 'test@test',
            password='test'
        )
        self.assertEqual(new_user= 'Test User')
        
        self.work_space_test = WorkSpaces.objects.create(
            name='Test WorkSpace'            
        )
        self.assertEqual(self.work_space_test.name,'Test WorkSpace')
        
        self.user_workspace_role = RolAssignment.objects.create(
            user= self.new_user,
            work_space = self.work_space_test,
            rol = 'CREATOR_WORK_SPACE'
        )
        self.assertEqual(self.user_workspace_role.rol,'CREATOR_WORK_SPACE')
        
        
        self.project1 = Project.objects.create(
            created_by_user = self.new_user,
            in_work_space= self.work_space_test,
            name= 'Project Test1',
            dead_line = '2023-10-20'
            )
        
        