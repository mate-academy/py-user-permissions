from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from rest_framework.views import View
from typing import Any


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        if view.basename == "order":
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff
