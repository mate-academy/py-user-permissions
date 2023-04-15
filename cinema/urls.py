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
router.register("movies", MovieViewSet),
router.register("orders", OrderViewSet, basename="order"),

urlpatterns = [
    path("actors/", ActorViewSet.as_view(), name="actor-list"),
    path("cinemahalls/", CinemaHallViewSet.as_view(), name="cinemahall-list"),
    path("genres/", GenreViewSet.as_view(), name="genre-list"),
    path("", include(router.urls)),
]

app_name = "cinema"
