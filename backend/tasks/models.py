import uuid

from django.contrib.auth.models import User
from django.db import models

from common.behaviors import TimestampedModel


class TaskList(TimestampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(TimestampedModel):
    tasklist = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True, editable=False)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    complete = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, default=None, editable=False)
