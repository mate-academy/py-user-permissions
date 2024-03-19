from django.urls import path

from user.views import CreateUserView, CreateTokenView, RetrieveUpdateUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", RetrieveUpdateUserView.as_view(), name="manage")
]

app_name = "user"
