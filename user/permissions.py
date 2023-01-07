from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    methods = SAFE_METHODS

    def has_permission(self, request, view):
        private_user = bool(
            request.method in self.methods
            and request.user
            and request.user.is_authenticated
        )
        admin_user = bool(request.user and request.user.is_staff)
        return any([private_user, admin_user])


class OrderPostPermission(IsAdminOrIfAuthenticatedReadOnly):
    methods = SAFE_METHODS + ("POST",)
