from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Task, Comment, ActivityLog



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source='project.name')
    assignee = serializers.ReadOnlyField(source='assignee.username')
    class Meta:
        model = Task
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    class Meta:
        model = Comment
        fields = ['id', 'user', 'project', 'task', 'content', 'created_at', 'updated_at']

class ActivityLogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = ActivityLog
        fields = '__all__'                
