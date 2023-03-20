from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        # if request.user.is_superuser:
        #     return True
        # if request.user.is_authenticated and request.method in SAFE_METHODS:
        #     return True
        # return False
        return bool(
            (request.method in SAFE_METHODS and
            # request.user and
            request.user.is_authenticated) or
            (request.user.is_staff)
        )
