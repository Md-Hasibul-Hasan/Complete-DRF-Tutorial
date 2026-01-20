from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    # view level permission: List, Create
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    # object level permission: Retrieve, Update, Destroy
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False
    