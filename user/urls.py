from django.urls import path

from cinema.views import CreateUserView, CreateTokenView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("login/", CreateTokenView.as_view(), name="login"),
]

app_name = "user"
