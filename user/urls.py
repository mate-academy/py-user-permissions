from django.urls import path

from user.views import CreateUserView, UserView, LoginUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("me/", UserView.as_view(), name="manage"),
]

app_name = "user"
