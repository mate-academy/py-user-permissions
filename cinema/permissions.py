from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    Permission allows administrators full access (read and write),
    while regular authenticated users have read-only access
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(
                request.method
                in SAFE_METHODS
                and request.user.is_authenticated
            ) or request.user.is_staff
