from django.urls import path
from user.views import CreateUserView, CreateTokenView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view()),
    path("login/", CreateTokenView.as_view()),
    path("me/", ManageUserView.as_view()),
]

app_name = 'user'
