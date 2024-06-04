from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request: Request, view: APIView) -> bool:
        return bool(
            request.method in SAFE_METHODS and request.user
            and request.user.is_authenticated
        ) or (
            request.user and request.user.is_staff
        )
