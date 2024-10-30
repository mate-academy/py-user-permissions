# write your code here
from django.urls import path

from user.views import CreateTokenView, ManageUserView, CreateUserView

urlpatterns = [
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("register/", CreateUserView.as_view(), name="create"),
]

app_name = "user"
