from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IfAuthenticatedOrderReadAndCreate(permissions.BasePermission):
    """
    Permission class that allows:
    - Create new order for the authenticated users
    """

    def has_permission(self, request, view):
        # Allow read and create access for authenticated users
        if (
            request.method in SAFE_METHODS
            or request.method == "POST"
        ):
            return bool(request.user and request.user.is_authenticated)

        # Allow full access for admin users except deletion
        if (
                request.user
                and request.user.is_staff
                and request.method != "DELETE"
        ):
            return True

        return False


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    """
    Permission class that allows:
    - Read-only access to authenticated users
    - Full access to admin users
    """

    def has_permission(self, request, view):
        # Allow read-only access for authenticated users
        if (
            request.method in SAFE_METHODS
        ):
            return bool(request.user and request.user.is_authenticated)

        # Allow full access for admin users except deletion
        if (
            request.user
            and request.user.is_staff
            and request.method != "DELETE"
        ):
            return True

        return False
