from django.urls import path

from user.views import UserCreateView, UserLoginView, ManageUserView

app_name = "user"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="login"),
    path("login/", UserLoginView.as_view(), name="obtain-token"),

    path("me/", ManageUserView.as_view(), name="me"),
]
