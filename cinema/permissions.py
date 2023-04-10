from django.http import HttpRequest
from django.views import View
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(
            self,
            request: HttpRequest,
            view: View
    ) -> bool:
        if (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
        ):
            return True
        if request.user and request.user.is_staff:
            return True
        return False
