from django.urls import path

from user.views import UserCreateView, UserLoginView, UserUpdateView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", UserUpdateView.as_view(), name="manage")
]

app_name = "user"
