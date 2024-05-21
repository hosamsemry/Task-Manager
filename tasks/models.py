from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='tasks')
    assign = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True, related_name='tasks')    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.task.title}'

class ActivityLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='activity_logs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_logs')
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} {self.action} on {self.task.title}'