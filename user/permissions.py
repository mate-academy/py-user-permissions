from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ("GET", "PUT", "PATCH", "HEAD", "OPTIONS"):
            return bool(request.user and request.user.is_authenticated)
        else:
            raise MethodNotAllowed(request.method)


class IsAuthenticatedListCreate(BasePermission):
    def has_permission(self, request, view):
        if view.action == "list":
            return request.user and request.user.is_authenticated
        elif view.action == "create":
            return (
                request.user
                and request.user.is_authenticated
                and request.user.is_staff
            )
        else:
            raise NotFound()
