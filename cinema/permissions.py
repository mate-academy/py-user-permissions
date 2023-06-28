from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    Admin is able to do all request
    Authenticated users are able to read only (list, retrieve)
    """

    def has_permission(self, request, view):
        # SAFE_METHODS = list and retrieve
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            # If POST request is sent by non staff member:
            # (False) or (False) because request.method
            # in SAFE_METHODS is FALSE and
            # request.user.is_staff is also FALSE
            or (request.user and request.user.is_staff)
        )
