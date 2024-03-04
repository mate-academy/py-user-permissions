from django.urls import path

from user.views import CreateUserView, CreateTokenView, CreateManageView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
]

urlpatterns += [
    path("login/", CreateTokenView.as_view(), name="login")
]

urlpatterns += [
    path("me/", CreateManageView.as_view(), name="manage")
]

app_name = "user"
