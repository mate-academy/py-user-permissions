from django.urls import path

from user.views import UserCreateView, CreateTokenView, UserManageView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", UserManageView.as_view(), name="manage")
]

app_name = "user"
