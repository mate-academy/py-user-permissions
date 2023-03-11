from django.http import HttpRequest
from django.views import View
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request: HttpRequest, view: View) -> bool:
        """
        The request is authenticated as an admin user,
        or is a read-only request for non-admin users.
        """
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )
