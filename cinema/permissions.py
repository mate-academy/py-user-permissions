from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (
                request.method in SAFE_METHODS
                and request.user
                and request.user.is_authenticated
            )
            or (request.user and request.user.is_staff)
        )


class IsAdminOrAuthenticatedCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == "POST":
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
