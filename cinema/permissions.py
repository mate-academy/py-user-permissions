from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import NotFound


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                    request.method in SAFE_METHODS
                    and request.user
                    and request.user.is_authenticated
            )
            or (request.method != "DELETE" and request.user and request.user.is_staff)
        )


class IsAuthenticatedCreate(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                    (request.method in SAFE_METHODS or request.method == "POST")
                    and request.user
                    and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class IsAdminOrIfAuthenticatedReadOnlyMovieSession(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                    request.method in SAFE_METHODS
                    and request.user
                    and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )
