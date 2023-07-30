from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAuthenticated
)


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):

        return (
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        raise NotFound("Not enough permission")


class MovieSessionReadWritePermissions(
    IsAdminOrIfAuthenticatedReadOnly, BasePermission
):

    def has_object_permission(self, request, view, obj):
        methods = ("DELETE", "PUT", "PATCH")
        return (
            (
                request.method in methods
                and request.user
                and request.user.is_staff
            ) or request.user.is_authenticated
        )


class MoviePermissions(
    IsAdminOrIfAuthenticatedReadOnly, BasePermission
):

    def has_object_permission(self, request, view, obj):
        if request.method in ("PUT", "DELETE"):
            raise MethodNotAllowed(request.method)

        return request.user and (
            request.user.is_staff
            or request.user.is_authenticated
        )


class OrderPermissions(
    IsAuthenticated, IsAdminOrIfAuthenticatedReadOnly
):
    pass
