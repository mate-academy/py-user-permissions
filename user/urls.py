from django.urls import path
from rest_framework.authtoken import views

from .views import CreateUserView, CreateTokenView, UpdateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", UpdateUserView.as_view(), name="manage")

]

app_name = "user"
