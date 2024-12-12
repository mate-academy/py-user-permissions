import logging

from rest_framework.permissions import BasePermission, SAFE_METHODS

logger = logging.getLogger(__name__)

class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    """
    The request is authenticated as admin is a read/write (except delete) request, or
    the request is authenticated a user is a read-only request.
    """
    def has_permission(self, request, view):
        try:
            if (
                    view.action == "list" or (
                        view.action == "retrieve"
                        and view.__class__.__name__ in (
                                "MovieViewSet",
                                "MovieSessionViewSet"
                        )
                    )
            ):
                return request.user and request.user.is_authenticated

            elif request.method == "POST":
                if view.__class__.__name__ == "OrderViewSet":
                    return request.user and request.user.is_authenticated
                return request.user and request.user.is_staff

            elif (request.method in ("PUT", "PATCH", "DELETE")
                  and view.__class__.__name__ == "MovieSessionViewSet"):
                return request.user and request.user.is_staff
            else:
                return False

        except AttributeError:
            logger.error("Authentication credentials were not provided.")


