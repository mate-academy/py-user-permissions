from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminAllORAuthenticatedORReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        auth_constraints = (
            request.method in SAFE_METHODS and user.is_authenticated
        )
        staff_constraints = user.is_staff
        return auth_constraints or staff_constraints
