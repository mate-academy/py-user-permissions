from django.urls import path

from user.views import CreateUserView, CreateTokenView, ManagerUserView

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManagerUserView.as_view(), name="manage"),
]
