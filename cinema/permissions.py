from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


# class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
#     """
#     Admin is able to do all request
#     Authenticated users are able to read only (list, retrieve)
#     """
#
#     def has_permission(self, request, view):
#         # SAFE_METHODS = list and retrieve
#         return bool(
#             (
#                     request.method in SAFE_METHODS and
#                     # False if POST request sent by non admin
#                     request.user and
#                     request.user.is_authenticated
#             )
#             # If POST request is sent by non staff member:
#             # (False) or (False) because request.method
#             # in SAFE_METHODS is FALSE and
#             # request.user.is_staff is also FALSE
#             or
#             (
#                     request.user and request.user.is_staff
#             )
#         )


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    Admin is able to do all request
    Authenticated users are able to list and create
    """

    def has_permission(self, request, view):
        if view.action in ("retrieve", "update", "partial_update", "destroy"):
            raise NotFound()
        return bool(
            (
                    view.action in ("list", "create") and
                    request.user and
                    request.user.is_authenticated
            )
            or
            (
                    request.user and request.user.is_staff
            )
        )


class IsAuthenticatedOrNotFound(IsAuthenticated):
    """
    Allows access only to authenticated users.
    Raises 404 error if the user is not authenticated.
    """

    def has_permission(self, request, view):
        if not super().has_permission(request, view):
            raise PermissionDenied()

        return True


# class ListCreateRetrieve(BasePermission):
#     """
#     Admin is able to do all request
#     Authenticated users are able to list and create
#     """
#
#     def has_permission(self, request, view):
#         return bool(
#             (
#                     view.action in ("list", "create", "retrieve") and
#                     request.user and
#                     request.user.is_authenticated
#             )
#             or
#             (
#                     request.user and request.user.is_staff
#             )
#         )
