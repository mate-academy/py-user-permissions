from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieDetailView,
    MovieListView,
    MovieSessionViewSet,
    OrderViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("cinema_halls", CinemaHallViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>", MovieDetailView.as_view(), name="movie-detail"),
]

app_name = "cinema"
