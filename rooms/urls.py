from rest_framework.routers import DefaultRouter

from rooms import viewsets

router = DefaultRouter()
router.register("", viewsets.RoomViewSet, basename="room")


urlpatterns = router.urls
