from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    """
    Permission class that allows:
    - Read-only access to authenticated users
    - Full access to admin users
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_staff)


class IsAuthenticatedOrderCreate(permissions.BasePermission):
    """
    Permission class that allows:
    - Authenticated users to create orders
    - Admin users to read, create and update orders (no deletion)
    """
    def has_permission(self, request, view):
        if request.method == "POST":
            return bool(request.user and request.user.is_authenticated)
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        if request.user and request.user.is_staff and request.method != "DELETE":
            return True
        return False
