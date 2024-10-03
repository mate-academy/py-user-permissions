from django.urls import path, include
from rest_framework.authtoken import views


from user.views import UserCreateView, LoginUserView, ManageUserView

app_name = "user"

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage")
]
