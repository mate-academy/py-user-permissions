from django.urls import path

from user.views import CreateUserApiView, ManageUserApiView
from rest_framework.authtoken import views
urlpatterns = [
    path("register/", CreateUserApiView.as_view(), name="create"),
    path("login/", views.obtain_auth_token, name="login"),
    path("me/", ManageUserApiView.as_view(), name="manage")
]

app_name = "user"
