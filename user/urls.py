from django.urls import path
from rest_framework import routers

from user.views import CreateUserView, CreateTokenView, ManageUserView, OrderViewSet

router = routers.DefaultRouter()
router.register("orders", OrderViewSet)


urlpatterns = [
	path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="token"),
    path("me/", ManageUserView.as_view(), name="manage"),
]

urlpatterns += router.urls
