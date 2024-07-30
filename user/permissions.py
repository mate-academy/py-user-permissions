from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        condition_1 = (
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        )
        condition_2 = request.user and request.user.is_staff
        return bool(condition_1 or condition_2)
