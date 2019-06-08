from rest_framework import viewsets
from .serializers import TaskListSerializer, TaskSerializer, SharingSerializer

from .models import TaskList, Task, Sharing


class TaskListViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = TaskListSerializer

    def get_queryset(self):
        return TaskList.get_allowed_for_user(self.request.user) \
            .prefetch_related('owner') \
            .prefetch_related('tasks__created_by')


class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = TaskSerializer

    def get_queryset(self):
        allowed_lists = TaskList.get_allowed_for_user(self.request.user)
        return Task.objects.filter(tasklist__in=allowed_lists.values_list('id')) \
            .prefetch_related('created_by')


class SharingViewSet(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    serializer_class = SharingSerializer

    def get_queryset(self):
        owned_lists = TaskList.objects.filter(owner=self.request.user)
        return Sharing.objects.filter(tasklist__in=owned_lists)
