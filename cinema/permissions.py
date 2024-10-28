from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    Permission to allow only admin users to create, update, or delete data.
    Authenticated users can view data but cannot modify it.
    """

    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user.is_authenticated
            )
            or request.user.is_staff
        )
