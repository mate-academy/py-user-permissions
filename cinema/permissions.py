from rest_framework.permissions import BasePermission

class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    Custom permission: Only admins have full access, while authenticated users have read-only access.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False  # Ensure unauthenticated users get 401
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user.is_staff
