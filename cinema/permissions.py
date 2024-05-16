from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user:
            return True
        elif request.user and request.user.is_staff:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and not request.user.is_staff:
            if obj.user == request.user:
                return True
        if request.user.is_authenticated and request.user.is_staff:
            return True
        return False
