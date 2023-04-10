from django.urls import path

from user.views import UserCreateView, TokenCreateView, UserManageView

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="create"),
    path("login/", TokenCreateView.as_view(), name="login"),
    path("me/", UserManageView.as_view(), name="manage")
]

app_name = "user"
