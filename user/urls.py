from django.urls import path

from user.views import UserCreateAPIView, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("manage/", ManageUserView.as_view(), name="manage")
]

app_name = "user"
