from django.urls import include, path
from rest_framework.authtoken.views import ObtainAuthToken
from .views import UserCreateView, ManageUserView

urlpatterns = [
    path("register/", UserCreateView.as_view(), name="create"),
    path("login/", ObtainAuthToken.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage")
]

app_name = "user"
