from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse


User = get_user_model()


class TaskModelTest(TestCase):
    '''Model Test'''
    def test_task_str(self):
        user = User.objects.create_user(username='ashka', password='pass')
        task = Task.objects.create(title='Task Task', author=user)
        self.assertEqual(str(task), 'Task Task')
        

class TaskAPITest(APITestCase):

    def setUp(self):
        '''Setup authenticated client for view test'''
        self.user = User.objects.create_user(username='ashka', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(title='My Task', completed=False, author=self.user)
        
    def test_list_tasks(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)  

    def test_create_task(self):
        data = {'title': 'New Task'}
        response = self.client.post('/api/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        
    def test_get_single_task(self):
        response = self.client.get(f'/api/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'My Task')
        
    def test_update_task(self):
        data = {'title': 'Updated', 'completed': True}
        response = self.client.put(f'/api/{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated')
        self.assertTrue(self.task.completed)
        
    def test_delete_task(self):
        response = self.client.delete(f'/api/{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
        
    def test_filter_completed(self):
        self.task.completed = True
        self.task.save()
        response = self.client.get('/api/?completed=true')
        self.assertEqual(len(response.data["results"]), 1)

        response = self.client.get('/api/?completed=false')
        self.assertEqual(len(response.data["results"]), 0)

    def test_filter_title(self):
        response = self.client.get('/api/?title=my')
        self.assertEqual(len(response.data["results"]), 1)
        
    def test_auth_required(self):
        self.client.logout()
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)