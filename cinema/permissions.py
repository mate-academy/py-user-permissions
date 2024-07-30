from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        condition_auth_read_only = (
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        )
        condition_admin = request.user and request.user.is_staff

        return bool(condition_auth_read_only or condition_admin)
