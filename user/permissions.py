from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        # If the user is an admin, we allow everything.
        if request.user and request.user.is_staff:
            return True

        # If the request is "read" (GET/HEAD/OPTIONS), then we allow authenticated
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        # Everything else (POST, PUT, PATCH, DELETE) is prohibited
        return False
