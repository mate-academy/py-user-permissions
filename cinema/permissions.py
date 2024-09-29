from django.contrib.auth import authenticate
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        auth_constraints = all(
            (request.method in SAFE_METHODS, user, user.is_authenticated)
        )
        staff_constraints = all((user, user.is_staff))
        return auth_constraints or staff_constraints
