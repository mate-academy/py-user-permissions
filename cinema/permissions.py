from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import View


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        is_authenticated = request.user and request.user.is_authenticated
        if request.method in SAFE_METHODS:
            return is_authenticated
        if request.method == "POST" and view.basename == "order":
            return is_authenticated
        return request.user and request.user.is_staff
