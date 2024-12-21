from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import NotAuthenticated


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise NotAuthenticated()

        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True

        return request.user.is_staff
