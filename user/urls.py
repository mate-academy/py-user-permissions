from django.urls import path

from user.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", CreateTokenView.as_view(), name="create"),
    path("login/", CreateUserView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
