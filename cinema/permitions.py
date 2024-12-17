from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as a admin_user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if request.method == "DELETE":
            return False
        return bool(
            (request.user and request.user.is_authenticated and
             request.method in SAFE_METHODS) or
            (request.user and request.user.is_staff)
        )


class IsAuthenticatedReadOrCreate(BasePermission):
    """
    The user is authenticated and can create  read request.
    """

    def has_permission(self, request, view):

        return bool(
            request.method in SAFE_METHODS or
            request.method == "POST" and
            request.user.is_authenticated
        )