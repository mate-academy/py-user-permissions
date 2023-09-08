from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            True if request.user and request.user.is_staff
            or request.user and request.user.is_authenticated
            and request.method in permissions.SAFE_METHODS else False
        )
