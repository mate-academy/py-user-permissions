from django.urls import path

from .views import UserCreateView, CreateTokenView


urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token")
]

app_name = "user"
