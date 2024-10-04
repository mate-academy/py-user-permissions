from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        auth_constraints = all(
            [
                request.method in SAFE_METHODS,
                request.user.is_authenticated
            ]
        )
        return auth_constraints or request.user.is_staff