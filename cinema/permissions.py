from django.views import View
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    If is authenticated as an admin - read/write;
    if is authenticated as a user - read only.
    """

    def has_permission(self, request: Request, view: View) -> bool:
        return (
            (request.method in SAFE_METHODS and request.user.is_authenticated)
            or request.user.is_staff
        )
