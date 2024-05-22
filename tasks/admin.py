from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Project, Task, Comment, ActivityLog
from django import forms


# Register the built-in User model using the built-in UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Project)
class AdminProject(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'owner__username')


@admin.register(Task)
class AdminTask(admin.ModelAdmin):
    list_display = ('title', 'project', 'assign', 'status', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'project__name', 'assign__username')




from django import forms
from .models import Project, Task, Comment   
                       
@admin.register(Comment)
class AdminComment(admin.ModelAdmin):   
    list_display = ('task', 'user', 'created_at', 'updated_at')
    search_fields = ('task__title', 'user__username')

@admin.register(ActivityLog)
class AdminActivityLog(admin.ModelAdmin):
    list_display = ('task', 'user', 'action', 'timestamp')
    search_fields = ('task__title', 'user__username')        
