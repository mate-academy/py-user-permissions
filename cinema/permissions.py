from venv import create

from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class ListAndCreateOnly(IsAdminOrIfAuthenticatedReadOnly):
    def has_permission(self, request, view):
        if view.action in ("list", "create"):
            return True
        super().has_permission(request, view)
