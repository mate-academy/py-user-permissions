from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import NotAuthenticated


class CustomAuthentication(TokenAuthentication):
    def authenticate(self, request):
        result = super().authenticate(request)
        if result is None:
            raise NotAuthenticated()
        return result
