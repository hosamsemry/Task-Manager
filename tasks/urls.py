from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import  ProjectListCreateView,\
      ProjectDetailView, TaskListCreateView, TaskDetailView, CommentListCreateView, CommentDetailView, ActivityLogListView



urlpatterns = [
    #path('register/', RegisterView.as_view(), name='register'),
    #path('login/', CustomAuthToken.as_view(), name='token_obtain'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('activity-logs/', ActivityLogListView.as_view(), name='activity-log-list'),
]
