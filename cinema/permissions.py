from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or bool(
            request.user
            and request.user.is_staff
        )
