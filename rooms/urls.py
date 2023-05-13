from rest_framework.routers import DefaultRouter

from rooms import views

router = DefaultRouter()
router.register("", views.RoomViewSet)


urlpatterns = router.urls
