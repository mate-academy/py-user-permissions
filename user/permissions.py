
from rest_framework.permissions import BasePermission, SAFE_METHODS


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


class IsAdminOrIfAuthenticatedListCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return request.user and request.user.is_authenticated
        if request.method == "delete":
            return False
        return IsAdminOrIfAuthenticatedReadOnly

    def has_object_permission(self, request, view, obj):
        return False


class IsAdminOrIfAuthenticatedCRUD(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list", "create", "update", "partial_update", "delete"]:
            return request.user and request.user.is_authenticated
        return IsAdminOrIfAuthenticatedReadOnly
