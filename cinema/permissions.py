from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in [*SAFE_METHODS, "POST"]
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


class IsAdminOrIfAuthenticatedReadRetrieveOnly(
    IsAdminOrIfAuthenticatedReadOnly
):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated
