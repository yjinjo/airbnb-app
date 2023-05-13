from django.urls import path

from rooms import views

app_name = "rooms"

urlpatterns = [
    path("", views.RoomsView.as_view()),
    path("search/", views.room_search),
    path("<int:pk>/", views.RoomView.as_view()),
]
