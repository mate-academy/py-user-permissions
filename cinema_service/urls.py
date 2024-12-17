from django.contrib import admin
from django.urls import path, include
from user.urls import app_name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/cinema/", include("cinema.urls", namespace="cinema")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/user/", include("user.urls", namespace=app_name)),
]
