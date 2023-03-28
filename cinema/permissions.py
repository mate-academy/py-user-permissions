from rest_framework.permissions import BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as an admin, or is a read-only user request.
    """
    SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

    def has_permission(self, request, view) -> bool:
        return bool(
            (
                request.method in self.SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class IsAdminOrIfAuthenticatedReadCreateOnly(IsAdminOrIfAuthenticatedReadOnly):
    """
    Modification for Order.
    """
    SAFE_METHODS = ("GET", "HEAD", "OPTIONS", "POST")
