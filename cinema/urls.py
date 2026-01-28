from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cinema.views import (
    ActorDetailAPIView,
    ActorListCreateAPIView,
    CinemaHallViewSet,
    GenreDetailAPIView,
    GenreListCreateAPIView,
    MovieViewSet,
)

router = DefaultRouter()
router.register("cinema_halls", CinemaHallViewSet, basename="cinema-halls")
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    # Genre (APIView)
    path("genres/", GenreListCreateAPIView.as_view(),
         name="genre-list-create"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(),
         name="genre-detail"),
    # Actor (GenericAPIView)
    path("actors/", ActorListCreateAPIView.as_view(),
         name="actor-list-create"),
    path("actors/<int:pk>/", ActorDetailAPIView.as_view(),
         name="actor-detail"),
    # CinemaHall + Movie (routers)
    path("", include(router.urls)),
]
