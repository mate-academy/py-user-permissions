from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated):
            return True

        return request.user.is_authenticated and request.user.is_staff


class OrderPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
                and request.user.is_authenticated):
            return True

        return request.user.is_authenticated or request.user.is_staff
