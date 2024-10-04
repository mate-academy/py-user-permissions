from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(
            request.method in SAFE_METHODS and user.is_authenticated
        ) or user.is_staff
