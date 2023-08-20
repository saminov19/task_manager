from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from .models import User, Role, Task
from .serializers import UserSerializer, RoleSerializer, TaskSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['put'])
    def update_user(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(user, data=request.data)
        
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to update users.'}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_user(self, request, pk=None):
        user = self.get_object()
        
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to delete users.'}, status=status.HTTP_403_FORBIDDEN)
        
        user.delete()
        return Response({'detail': 'User deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)




class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['put'])
    def update_role(self, request, pk=None):
        role = self.get_object()
        serializer = RoleSerializer(role, data=request.data)
        
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to update roles.'}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_role(self, request, pk=None):
        role = self.get_object()
        
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to delete roles.'}, status=status.HTTP_403_FORBIDDEN)
        
        role.delete()
        return Response({'detail': 'Role deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy', 'assign_task']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
    
    
    @action(detail=True, methods=['post'])
    def assign_task(self, request, pk=None):
        task = self.get_object()
        assigned_to = request.data.get('assigned_to')
        
        if not request.user.is_authenticated:
            return Response({'detail': 'You must be logged in to assign tasks.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if request.user != task.created_by and request.user != assigned_to:
            return Response({'detail': 'You do not have permission to assign this task.'}, status=status.HTTP_403_FORBIDDEN)
        
        task.assigned_to = assigned_to
        task.save()

        # Send email notification asynchronously via Celery
        send_task_assignment_email.delay(assigned_to.email, task.title)

        return Response({'detail': 'Task assigned successfully.'}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['get'])
    def list_tasks(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    @action(detail=True, methods=['put'])
    def update_task(self, request, pk=None):
        task = self.get_object()
        serializer = TaskSerializer(task, data=request.data)
        
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to update tasks.'}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['delete'])
    def delete_task(self, request, pk=None):
        task = self.get_object()
        
        if not request.user.is_staff:
            return Response({'detail': 'You do not have permission to delete tasks.'}, status=status.HTTP_403_FORBIDDEN)
        
        task.delete()
        return Response({'detail': 'Task deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)








