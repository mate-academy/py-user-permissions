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
router.register("orders", OrderViewSet)
router.register("movies", MovieViewSet),
router.register("actors", ActorViewSet),
router.register("genres", GenreViewSet),
router.register("cinema_halls", CinemaHallViewSet),
router.register("movie_session", MovieSessionViewSet)

urlpatterns = router.urls

app_name = "cinema"
