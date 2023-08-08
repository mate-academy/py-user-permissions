from rest_framework.exceptions import NotFound, MethodNotAllowed
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        if (
            request.method in SAFE_METHODS
            and not view.action == "retrieve"
        ):
            return bool(
                (request.user.is_authenticated and request.user)
            )
        elif request.method == "POST":
            return bool(
                request.user and request.user.is_staff
            )
        raise NotFound(detail="Not found")


class IsAdminOrIfAuthenticatedReadAndRetrieve(BasePermission):
    def has_permission(self, request, view) -> bool:
        if (
            request.method in SAFE_METHODS
        ):
            return bool(
                (request.user.is_authenticated and request.user)
            )
        elif request.method == "POST":
            return bool(
                request.user and request.user.is_staff
            )
        raise MethodNotAllowed(method=request.method)


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(
            (
                request.user
                and request.user.is_staff
            ) or (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
        )


class IsAdminOrIfAuthenticatedAndPost(BasePermission):
    def has_permission(self, request, view) -> bool:
        if (
            request.method in SAFE_METHODS
            and view.action != "retrieve"
        ):
            return bool(
                (
                    request.user.is_authenticated
                    and request.user
                )
            )
        elif request.method == "POST":
            return bool(
                (request.user and request.user.is_staff)
                or (
                    request.user
                    and request.user.is_authenticated
                )
            )
        raise NotFound(detail="Not found")
