from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as a admin_user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            (
                request.user
                and request.user.is_authenticated
                and request.method in SAFE_METHODS
            )
            or (request.user and request.user.is_staff)
        )


class OrderPermission(BasePermission):
    """
    The authenticated user can create. And only owner can observe
    """

    def has_permission(self, request, view):

        return bool(
            (request.method == "POST" or request.method in SAFE_METHODS)
            and request.user
            and (request.user.is_authenticated or request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):

        return bool(
            request.user
            and request.user.is_authenticated
            and request.method in SAFE_METHODS
            and request.user == obj.user
        )
