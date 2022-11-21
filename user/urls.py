from django.urls import path

from user.views import CreateUserView, ObtainTokenView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", ObtainTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
