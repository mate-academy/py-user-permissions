from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """The request is authenticated as an admin - read/write,
    if as a user - read only request"""

    def has_permission(self, request, view):
        view_name = view.__class__.__name__
        view_action = view.action

        if view_name in [
            "ActorViewSet",
            "GenreViewSet",
            "CinemaHallViewSet",
        ] and view_action in ["retrieve", "destroy", "update"]:
            raise NotFound("Object not found.")

        if view_name == "MovieSessionViewSet":
            return bool(
                view_action in ("list", "retrieve")
                and request.user
                and request.user.is_authenticated
            ) or (request.user and request.user.is_staff)

        return bool(
            view_action == "list"
            and request.user
            and request.user.is_authenticated
        ) or (request.user and request.user.is_staff)


class ReadCreateOnly(BasePermission):

    def has_permission(self, request, view):
        if view.action in ["destroy", "update"]:
            raise MethodNotAllowed(
                method=request.method,
                detail="Method not allowed for this action."
            )

        return bool(
            request.method in SAFE_METHODS
            and request.user
            and request.user.is_authenticated
        ) or (
            request.method in ("GET", "POST")
            and request.user
            and request.user.is_staff
        )


class ReadAndCreateIfAuthenticated(BasePermission):

    def has_permission(self, request, view):
        if view.action in ["delete", "update", "retrieve", "destroy"]:
            raise NotFound("Object not found.")

        return bool(
            request.method in ("GET", "POST")
            and request.user
            and request.user.is_authenticated
        )
