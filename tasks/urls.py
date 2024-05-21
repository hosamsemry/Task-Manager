from django.urls import path
from .views import RegisterView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    ProjectListCreateView, ProjectDetailView,
    TaskListCreateView, TaskDetailView,
    CommentListCreateView, CommentDetailView,
    ActivityLogListView,RegisterView, MyTokenObtainPairView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('activity-logs/', ActivityLogListView.as_view(), name='activity-log-list'),
]
