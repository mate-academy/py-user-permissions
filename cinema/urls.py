from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreListCreateViewSet,
    ActorListCreateViewSet,
    CinemaHallListCreateView,
    MovieListCreateRetrieveViewSet,
    MovieSessionListCreateUpdateDeleteViewSet,
    OrderListCreateViewSet,
)


router = routers.DefaultRouter()

router.register("genres", GenreListCreateViewSet)
router.register("actors", ActorListCreateViewSet)
router.register("cinema_halls", CinemaHallListCreateView)
router.register("movies", MovieListCreateRetrieveViewSet)
router.register("movie_sessions", MovieSessionListCreateUpdateDeleteViewSet)
router.register("orders", OrderListCreateViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
