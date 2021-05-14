from django.urls import path, include

from rest_framework import routers

from .views import BreedViewSet, ImageViewSet, FavouriteViewSet, VoteViewSet

router = routers.DefaultRouter()

router.register("breeds", BreedViewSet)
router.register("images", ImageViewSet)
router.register("favourites", FavouriteViewSet)
router.register("votes", VoteViewSet)


urlpatterns = [
    path("", include(router.urls))
]
