from rest_framework import viewsets
from .serializers import TaskListSerializer, TaskSerializer

from .models import TaskList, Task


def get_allowed_tasklists(user):
    return TaskList.objects.filter(owner=user) \
        .union(TaskList.objects.filter(shared_with__in=[user]))


class TaskListViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return get_allowed_tasklists(self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = TaskSerializer

    def get_queryset(self):
        allowed_lists = get_allowed_tasklists(self.request.user)
        return Task.objects.filter(tasklist__in=allowed_lists)
