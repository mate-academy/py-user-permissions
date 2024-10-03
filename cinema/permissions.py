from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as ad admin - read/write,
    if as a user - read only.
    """
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            and request.user.is_authenticated
        ) or request.user.is_staff
