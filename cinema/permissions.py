from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS and
            request.user and
            request.user.is_authenticated
        ) or (request.user and request.user.is_staff)


class IsAdminOrCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        return ((request.method in ("GET", "POST")
                and request.user.is_authenticated)
                or request.user.is_staff)
