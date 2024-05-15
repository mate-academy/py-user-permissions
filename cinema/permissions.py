from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminExceptDelete(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in ("GET", "PUT", "PATCH", "HEAD", "OPTIONS") and request.user and request.user.is_staff
        )


class IsAuthenticatedOwnOrders(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in ("GET", "PUT", "PATCH", "HEAD", "OPTIONS") and request.user and request.user.is_authenticated
        )