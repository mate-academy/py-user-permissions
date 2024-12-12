from django.urls import path

from user.views import CreateUserView, CreateTokenView, ManageUserView, OrderViewSet

urlpatterns = [
	path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("order/", OrderViewSet.as_view(), name="order"),
]

