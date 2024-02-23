from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.authentication import TokenAuthentication

from cinema.permissions import IsAdminOrIfAuthenticatedReadOnly


class ListCreateAuthMixin(
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ListCreateAuthMixinWithPermissions(ListCreateAuthMixin):
    def get_permissions(self):
        if self.action in ("list", "create"):
            return [IsAdminOrIfAuthenticatedReadOnly(), ]

        return []
