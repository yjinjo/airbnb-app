from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path("me/", views.MeView.as_view()),
    path("me/favs/", views.FavsView.as_view()),
    path("<int:pk>/", views.user_detail),
]
