from django.test import TestCase
from .models import User,UserProfile,WorkSpaces,RolAssignment
# Create your tests here.

class Test_UserCreation(TestCase):
    def test_creation_user_profile(self):
        self.test= UserProfile.objects.create_user(
             username='Test User',
                    email= 'test@test',
                    password='test'
        )
        
        
        self.assertEqual(self.test.username,'Test User')
      
    
        
        
    
class Test_WorkSpaceCreation(TestCase):
    def test_create_project(self):
        work_space_test = WorkSpaces.objects.create(
            name='Test WorkSpace'            
        )
        self.assertEqual(work_space_test.name,'Test WorkSpace')
        
class Test_RoleAssignement(TestCase):
    def test_RoleAssignement(self):
        self.new_user= UserProfile.objects.create_user(
            username='Test User',
            email= 'test@test',
            password='test'
        )
        self.assertEqual(self.new_user.username,'Test User')
       
        self.work_space_test = WorkSpaces.objects.create(
            name='Test WorkSpace'            
        )
        self.assertEqual(self.work_space_test.name,'Test WorkSpace')
        
        
        self.user_workspace_role = RolAssignment.objects.create(
            user= self.new_user,
            work_space = self.work_space_test,
            rol = 'CREATOR_WORK_SPACE'
        )
        self.assertEqual(self.user_workspace_role.user,self.new_user)
        self.assertEqual(self.user_workspace_role.work_space,self.work_space_test)
        self.assertEqual(self.user_workspace_role.rol,'CREATOR_WORK_SPACE')
        #usuario = Test_UserCreation.test_creation_user(self)'''
        
        