from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated
    if as a user - read request for all models and create for Order model,
    as an admin:
    Genre, Cinema Hall, Actor, Order - list and create,
    Movie - list, create and retrieve,
    Movie Session - list, retrieve, create, update, partial update, delete
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS and request.user.is_authenticated
        ) or request.user.is_staff
