from rest_framework import serializers
from .models import Project, Task, Comment, ActivityLog


class ProjectListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        fields = ['id' ,'name', 'owner', 'created_at', 'updated_at','due_date']

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        fields = '__all__'

class TaskListSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source='project.name')
    assignee = serializers.ReadOnlyField(source='assign.username')
    class Meta:
        model = Task
        fields = ['title','project', 'assignee', 'status', 'created_at', 'updated_at']

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source='project.name')
    assignee = serializers.ReadOnlyField(source='assign.username')
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'project', 'assignee', 'status', 'due_date', 'created_at', 'updated_at']



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    task = serializers.ReadOnlyField(source='task.title')
    project = serializers.ReadOnlyField(source='project.name')
    class Meta:
        model = Comment
        fields = ['id', 'user', 'project', 'task', 'content', 'created_at', 'updated_at']

class ActivityLogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = ActivityLog
        fields = '__all__'                
