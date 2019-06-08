from django.contrib import admin

from .models import Task, TaskList


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]
