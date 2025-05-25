from rest_framework import generics
from .serializers import TaskSerializers
from .models import Task
from .permissions import AuthorOnly


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (AuthorOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    
    
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
