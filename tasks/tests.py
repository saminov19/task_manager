from django.test import TestCase, Client
from rest_framework.test import APIClient
from .models import Task, User
from .serializers import TaskSerializer
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
import json

User = get_user_model()


class TaskModelTest(TestCase):
    def test_task_str(self):
        user1 = User.objects.create(email='user1@example.com', password='password1', first_name='User1', last_name='Last1', username='user1')
        user2 = User.objects.create(email='user2@example.com', password='password2', first_name='User2', last_name='Last2', username='user2')
        task = Task.objects.create(title='Test Task',
            description='test description',
            created_by_id=user1.id,
            assigned_to_id=user2.id)
        self.assertEqual(str(task), 'Test Task')

    def test_task_fields(self):
        user1 = User.objects.create(email='user1@example.com', password='password1', first_name='User1', last_name='Last1', username='user1')
        user2 = User.objects.create(email='user2@example.com', password='password2', first_name='User2', last_name='Last2', username='user2')
        # Create a task
        task = Task(
            title='test task',
            description='test description',
            created_by_id=user1.id,
            assigned_to_id=user2.id
        )
        
        self.assertEqual(task.title, 'test task')
        self.assertEqual(task.created_by_id, user1.id)
        self.assertEqual(task.assigned_to_id, user2.id)
        task.save()

        # read the saved tasks
        saved_task = Task.objects.get(pk=task.id)

        # check if data was saved correctly
        self.assertEqual(saved_task.title, 'test task')
        self.assertEqual(saved_task.description, 'test description')
        self.assertEqual(saved_task.created_by_id, user1.id)
        self.assertEqual(saved_task.assigned_to_id, user2.id)
        





class TaskSerializerTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            email='user1@example.com',
            password='password1',
            first_name='User1',
            last_name='Last1',
            username='user1'
        )
        
        self.user2 = User.objects.create(
            email='user2@example.com',
            password='password2',
            first_name='User2',
            last_name='Last2',
            username='user2'
        )
        
        self.task_data = {
            'title': 'Test Task',
            'description': 'Description',
            'created_by': self.user1,
            'assigned_to': self.user2
        }

    def test_task_serializer(self):
        task = Task.objects.create(**self.task_data)
        serializer = TaskSerializer(instance=task)

        self.assertEqual(serializer.data['title'], self.task_data['title'])
        self.assertEqual(serializer.data['description'], self.task_data['description'])
        self.assertEqual(serializer.data['created_by'], self.user1.id)
        self.assertEqual(serializer.data['assigned_to'], self.user2.id)








class TaskViewSetTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='user1@example.com', password='password1', first_name='User1', last_name='Last1', username='user1')
        self.user2 = User.objects.create(email='user2@example.com', password='password2', first_name='User2', last_name='Last2', username='user2')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user1) 
        self.task_data = {
            'title': 'Test Task',
            'description': 'Description',
            'created_by': self.user1,  
            'assigned_to': self.user2, 
        }
        self.task = Task.objects.create(**self.task_data)

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = reverse('task-list')

        
        self.task_data = {
            'title': 'Test Task',
            'description': 'Description',
            'created_by': self.user1.id, 
            'assigned_to': self.user2.id,  
        }
        # Serialize the task_data to JSON
        task_data_json = json.dumps(self.task_data)
        
        # turn task data to JSON
        response = self.client.post(url, task_data_json, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        
        task = Task.objects.get(id=2)
        self.assertEqual(task.title, self.task_data['title'])
        self.assertEqual(task.description, self.task_data['description'])
        self.assertEqual(task.created_by.id, self.user1.id)
        self.assertEqual(task.assigned_to.id, self.user2.id)
        


    def test_retrieve_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        updated_data = {'title': 'Updated Task'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
