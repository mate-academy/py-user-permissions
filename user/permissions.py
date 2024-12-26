from rest_framework.permissions import SAFE_METHODS, BasePermission


# class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         # If the user is an admin, we allow everything.
#         if request.user and request.user.is_staff:
#             return True
#
#         # If the request is "read" (GET/HEAD/OPTIONS),
#         # then we allow authenticated
#         if request.method in SAFE_METHODS:
#             return bool(request.user and request.user.is_authenticated)
#
#         # Allow POST to regular authenticated users
#         if (
#                 request.method == "POST"
#                 and request.user
#                 and request.user.is_authenticated
#         ):
#             return True
#
#         # Everything else (POST, PUT, PATCH, DELETE) is prohibited
#         return False
class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Разрешаем всё админам
        if request.user and request.user.is_staff:
            return True

        # Разрешаем GET/HEAD/OPTIONS аутентифицированным
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        # Иначе (POST/PUT/PATCH/DELETE) — запрещаем
        return False
