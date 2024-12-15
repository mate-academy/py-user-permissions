from rest_framework import permissions


class IsAdminOrIfAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated \
            if request.method in permissions.SAFE_METHODS\
            else request.user.is_staff
