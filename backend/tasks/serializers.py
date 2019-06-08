from rest_framework import serializers

from .models import TaskList, Task, Sharing


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Task
        fields = (
            'uuid',
            'created_by',
            'description',
            'details',
            'complete',
        )


class TaskListSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(read_only=True, slug_field='username')
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = (
            'uuid',
            'owner',
            'name',
            'tasks',
        )


class SharingSerializer(serializers.ModelSerializer):
    tasklist = serializers.SlugRelatedField(read_only=True, slug_field='uuid')
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    display_name = serializers.SerializerMethodField()

    def get_display_name(self, obj):
        return obj.tasklist.name

    class Meta:
        model = Sharing
        fields = (
            'uuid',
            'display_name',
            'tasklist',
            'user',
        )
