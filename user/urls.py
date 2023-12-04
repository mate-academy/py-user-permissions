from django.urls import path
from user.views import CreateUserView, CreateUserTokenView, ManageUserView


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateUserTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage")
]

app_name = "user"
