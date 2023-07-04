from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreListCreateView,
    ActorListCreateView,
    CinemaHallListCreateView,
    MovieViewSet,
    MovieSessionViewSet,
    OrderListCreateView,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreListCreateView.as_view(), name="genre-list"),
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path(
        "cinema_halls/",
        CinemaHallListCreateView.as_view(),
        name="cinemahall-list"
    ),
    path("orders/", OrderListCreateView.as_view(), name="order-list"),
]

app_name = "cinema"
