from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    Custom permission to only allow auth users to read and admin users to edit
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (request.user and request.user.is_staff)
