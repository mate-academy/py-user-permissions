from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(
    permissions.BasePermission
):
    """
    Default permission class which make only
    for admin user and all authenticated user
    possible to read data
    """
    def has_permission(self, request, view):
        return bool(
            request.method is SAFE_METHODS
            and (request.user and request.user.is_authenticated)
            or (request.user and request.user.is_staff)
        )
