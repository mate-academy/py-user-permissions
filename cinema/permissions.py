from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    DjangoModelPermissions,
)


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Authenticated users can read
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        # Only admin (staff) users can modify
        return request.user.is_staff


class ReadAndCreate(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(request.user and request.user.is_authenticated)


class NoPermission(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(
            request.user
            and request.user.is_authenticated
            and not request.user.is_staff
        )
