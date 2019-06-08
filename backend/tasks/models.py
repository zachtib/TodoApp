import uuid

from django.contrib.auth.models import User
from django.db import models

from common.behaviors import TimestampedModel


class TaskList(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_lists')
    name = models.CharField(max_length=50)
    shared_with = models.ManyToManyField(
        User,
        through='Sharing',
        through_fields=('tasklist', 'user'),
        related_name='shared_lists',
    )

    def __str__(self):
        return self.name


class Task(TimestampedModel):
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name='tasks')
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, default=None, editable=False)

    def __str__(self):
        return self.description

class Sharing(TimestampedModel):
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
