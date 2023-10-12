from django.urls import path

from .views import UserCreateViewSet, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", UserCreateViewSet.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

app_name = "user"
