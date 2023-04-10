from django.urls import path

from user.views import UserCreationView, TokenCreationView, UserManageView

urlpatterns = [
    path("register/", UserCreationView.as_view(), name="create"),
    path("login/", TokenCreationView.as_view(), name="login"),
    path("me/", UserManageView.as_view(), name="manage"),
]

app_name = "user"
