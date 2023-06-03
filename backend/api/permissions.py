from rest_framework import permissions

from users.models import UserRole


class RecipePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated):
            return True
        return None

    def has_object_permission(self, request, view, obj):
        if (request.user.is_authenticated
                and (obj.author == request.user
                     or request.user.role == UserRole.Admin
                     or request.user.is_superuser)):
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
