from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnlyListAndCreate(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                (
                    request.method in SAFE_METHODS
                    and request.user
                    and request.user.is_authenticated
                )
                or (request.user
                    and request.user.is_staff
                    and request.method == "POST")
            )
        )


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (
                request.user
                and request.user.is_staff
                and request.method in ("POST", "PUT", "PATCH", "DELETE")
            )
        )


class IsAdminOrIfAuthenticatedReadOnlyOrder(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                view.action in ("list", "create")
                and request.user
                and request.user.is_authenticated
            )
        )
