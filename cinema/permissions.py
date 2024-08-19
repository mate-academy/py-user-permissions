from rest_framework import permissions
from rest_framework.permissions import BasePermission


# unsafe (create, update, partial_update, destroy) ==   (POST, PUT, DELETE)
# safe   (list, retrieve) ==                            (GET, HEAD, OPTIONS)
# http_method_names = ["get", "post", "head", "options", "trace"]


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (request.user and request.user.is_staff)


class IsAdminOrIfAuthenticatedReadAndCreate(IsAdminOrIfAuthenticatedReadOnly):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated

        return super().has_permission(request, view)
