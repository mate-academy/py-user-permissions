from rest_framework import permissions

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedCreate(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ["list", "create"]:
            return request.user.is_authenticated
        elif view.action in ["list", "create"]:
            return request.user.is_staff


class IsAdminListCreate(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated
        elif view.action in ["list", "create"]:
            return request.user.is_staff


class IsAdminListCreateRetrieve(BasePermission):

    def has_permission(self, request, view):
        if view.action in ["list", "retrieve"]:
            return request.user.is_authenticated
        elif view.action in ["list", "create", "retrieve"]:
            return request.user.is_staff


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as an admin user, or is a read-only
    for non-admin users request.
    """

    def has_permission(self, request, view):

        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )

            or (request.user and request.user.is_staff)
        )
