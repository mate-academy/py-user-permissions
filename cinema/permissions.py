from rest_framework.permissions import BasePermission


class IfAdminCreateIfAuthReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (view.action == "list" and request.user.is_authenticated) or (
            view.action in ["list", "create"] and request.user.is_staff
        ):
            return True
        return False


class IfAdminCreateRetrieveIfAuthReadOnly(BasePermission):
    def has_permission(self, request, view):
        if (
            view.action in ["list", "retrieve"]
            and request.user.is_authenticated
        ):
            return True
        elif (
            view.action in ["create", "update", "destroy"]
            and request.user.is_staff
        ):
            return True
        return False


class IfAdminOrIfAuthReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action in ["list", "retrieve"]:
                return True
            elif request.user.is_staff:
                return True
        return False


class IfAuthReadCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list", "create"] and request.user.is_authenticated:
            return True
        return False
