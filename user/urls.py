from django.urls import path

from user.views import CreateUser, CreateAuthTokenView, ManageUserView

app_name = "user"

urlpatterns = [
    path("register/", CreateUser.as_view(), name="create"),
    path("login/", CreateAuthTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage")
]
