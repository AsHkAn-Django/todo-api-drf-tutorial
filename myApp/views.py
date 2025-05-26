from rest_framework import generics, viewsets
from .serializers import TaskSerializer
from .models import Task
from .permissions import AuthorOnly



class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (AuthorOnly,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        # for getting the querry parameter in drf use `self.request.query_params.get` instead of `self.request.GET.get()`
        # `self.request.GET.get()` still works in drf but not recommended
        completed = self.request.query_params.get('completed')
        title = self.request.query_params.get('title')
        
        # We check if the completed parameter is not empty(we don't say `if completed` because in that way we check the boolean)
        if completed is not None:
            # if the parameter is in this list (TRUE or 1)
            queryset = queryset.filter(completed=completed.lower() in ['true', '1'])
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (AuthorOnly,)
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
    
    
# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializers
