from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
    
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method in ['GET', 'HEAD', 'OPTIONS']
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.method in ['GET', 'HEAD', 'OPTIONS']    