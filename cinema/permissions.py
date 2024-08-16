from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and request.user.is_authenticated
        ) or request.user.is_staff


class IsAdminOrIfAuthenticatedReadAndCreate(IsAdminOrIfAuthenticatedReadOnly):
    def has_permission(self, request, view):
        if request.method == "POST":
            return request.user.is_authenticated

        return super().has_permission(request, view)
