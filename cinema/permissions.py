from django.http import Http404
from rest_framework.permissions import BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (
                view.action in ["retrieve", "list"]
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class OrderPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["retrieve", "update", "partial_update", "destroy"]:
            raise Http404
        if (
                view.action in ["create", "list"]
                and request.user and request.user.is_authenticated
        ):
            return True
