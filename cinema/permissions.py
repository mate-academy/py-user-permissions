from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        is_authenticated = request.user and request.user.is_authenticated
        if request.method in SAFE_METHODS:
            return is_authenticated
        if request.method == "POST" and view.basename == "order":
            return is_authenticated
        return request.user and request.user.is_staff
