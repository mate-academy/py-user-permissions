from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminAllORIsAuthenticatedOReadOnly(BasePermission):
    """
    The request is authenticated as a admin -
    read/write, if as a user - read only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (request.user and request.user.is_staff)


class IsAdminAllORIsAuthenticatedOReadOnly1(BasePermission):
    """
    The request is authenticated as a admin -
    read/write, if as a user - read only request.
    """
    def has_permission(self, request, view):

        if view.action in ["list", "create"]:
            return bool(
                (request.method in SAFE_METHODS
                 and request.user
                 and request.user.is_authenticated
                 )
                or (request.user and request.user.is_staff)
            )
        return bool(
            request.method in SAFE_METHODS
            or (request.user and request.user.is_staff)
        )
