from rest_framework import mixins
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.viewsets import GenericViewSet


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            (request.method in SAFE_METHODS
             and request.user
             and request.user.is_authenticated)
            or (request.user and request.user.is_staff)
        )


class ListCreateViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    pass


class ListCreateRetrieveViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    pass
