from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet,
    OrderViewSet,
)

#router = routers.DefaultRouter()
actors = ActorViewSet.as_view({'get': 'list', 'post': 'create'})
# router.register("genres", GenreViewSet)
# router.register("movies", MovieViewSet)
# router.register("cinema_halls", CinemaHallViewSet)
# router.register("movies", MovieViewSet)
# router.register("movie_sessions", MovieSessionViewSet)
# router.register("orders", OrderViewSet)

urlpatterns = [
path("actors/", actors, name="actor-list"),
    #path("", include(router.urls)),

]

app_name = "cinema"
