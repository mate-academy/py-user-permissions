from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (
                request.user and request.user.is_staff
            )

        )


class PermissionMixin:
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    def get_permissions(self):
        return [
            permission()
            for permission in self.permission_classes
            if self.action in self.permission_required_actions
        ]
