from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
      Custom permission class that grants different levels of access based on user role.

      - Full access is granted if the user is an admin.
      - Read-only access is granted if the user is authenticated but not an admin.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (
            request.user and request.user.is_staff
        )
