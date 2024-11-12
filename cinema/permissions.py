from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

            # Разрешить аутентифицированным пользователям доступ к безопасным методам (чтение)
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated

            # Разрешить аутентифицированным пользователям создание заказов (POST) только в OrderViewSet
        if (view.__class__.__name__ == "OrderViewSet"
                and request.method == "POST"):
            return request.user and request.user.is_authenticated

            # Запретить все остальные действия для неадминистраторов
        return False
