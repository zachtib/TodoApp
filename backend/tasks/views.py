from rest_framework import viewsets
from .serializers import TaskListSerializer, TaskSerializer

from .models import TaskList, Task


class TaskListViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.get_allowed_for_user(self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = TaskSerializer

    def get_queryset(self):
        allowed_lists = TaskList.get_allowed_for_user(self.request.user)
        return Task.objects.filter(tasklist__in=allowed_lists.values_list('id'))
