from django.urls import path

from user.views import ManageUserCreateView, UserLoginView, CreateUserView

app_name = "user"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("me/", ManageUserCreateView.as_view(), name="manage")
]
