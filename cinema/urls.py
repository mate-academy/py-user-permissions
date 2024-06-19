from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)
router.register("movies", MovieViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreViewSet.as_view(), name="genre-list"),
    path("cinema_halls/", CinemaHallViewSet.as_view(), name="cinemahall-list"),
    path("actors/", ActorViewSet.as_view(), name="actor-list"),
    path("orders/", OrderViewSet.as_view(), name="order-list"),
]

app_name = "cinema"
