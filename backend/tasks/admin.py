from django.contrib import admin

from .models import Task, TaskList, Sharing


class SharingInline(admin.TabularInline):
    model = Sharing


class TaskInline(admin.TabularInline):
    model = Task


@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
        SharingInline,
    ]
