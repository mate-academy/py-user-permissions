from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and \
                (request.user and request.user.is_authenticated):
            return True
        elif request.user and request.user.is_staff:
            return True
