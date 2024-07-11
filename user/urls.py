from django.urls import path

from user.views import CreateUserView, LoginUserView, MangerUserView


urlpatterns =[
    path("register/", CreateUserView.as_view(), name="register_user"),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("me/", MangerUserView.as_view(), name="manage_user"),
]

app_name = "user"
