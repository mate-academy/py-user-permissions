from django.urls import path

from user.views import CreateUserView

from rest_framework.authtoken import views

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", views.obtain_auth_token, name="get_token"),
]

app_name = "user"
