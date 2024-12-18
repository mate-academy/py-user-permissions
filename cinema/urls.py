from unittest.mock import patch

from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    # MovieDetailView,
    # MovieSessionDetailView,
)

# router = routers.DefaultRouter()
# router.register("genres", GenreViewSet)
# router.register("actors", ActorViewSet)
# router.register("cinema_halls", CinemaHallViewSet)
# router.register('movies', MovieViewSet, basename='movies')
# router.register("movie_sessions", MovieSessionViewSet)
# router.register("orders", OrderViewSet)

# urlpatterns = [path("", include(router.urls))]
# movies = MovieViewSet.as_view({'get': 'list', "post": "create",})
# movie = MovieViewSet.as_view({'get': 'retrieve'})

movie_list = MovieViewSet.as_view({"get": "list", "post": "create"})
movie_detail = MovieViewSet.as_view({"get": "retrieve"})
movie_session_list = MovieSessionViewSet.as_view(
    {"get": "list", "post": "create"}
)
movie_session_detail = MovieSessionViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("actors/", ActorViewSet.as_view(), name="actor-list"),
    path("cinema_hall/", CinemaHallViewSet.as_view(), name="cinemahall-list"),
    path("genres/", GenreViewSet.as_view(), name="genre-list"),
    path("movie_sessions/", movie_session_list, name="moviesession-list"),
    path(
        "movie_sessions/<int:pk>/",
        movie_session_detail,
        name="moviesession-detail",
    ),
    path("orders/", OrderViewSet.as_view(), name="order-list"),
]


app_name = "cinema"
