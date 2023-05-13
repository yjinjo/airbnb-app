from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet

from rooms.models import Room
from rooms.permissions import IsOwner
from rooms.serializers import RoomSerializer


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_permissions(self):
        # GET /rooms/ or GET /room/1/
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [permissions.AllowAny]
        elif self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        # DELETE /room/1/ PUT /room/1/
        else:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]


@api_view(["GET"])
def room_search(request):
    max_price = request.GET.get("max_price", None)
    min_price = request.GET.get("min_price", None)
    beds = request.GET.get("beds", None)
    bedrooms = request.GET.get("bedrooms", None)
    bathrooms = request.GET.get("bathrooms", None)
    lat = request.GET.get("lat", None)
    lng = request.GET.get("lng", None)
    filter_kwargs = {}
    if max_price:
        filter_kwargs["price__lte"] = max_price
    if min_price:
        filter_kwargs["price__gte"] = min_price
    if beds:
        filter_kwargs["beds__gte"] = beds
    if bedrooms:
        filter_kwargs["bedrooms__gte"] = bedrooms
    if bathrooms:
        filter_kwargs["bathrooms__gte"] = bathrooms
    if lat and lng:
        filter_kwargs["lat__gte"] = float(lat) - 0.005
        filter_kwargs["lat__lte"] = float(lat) + 0.005
        filter_kwargs["lng__gte"] = float(lng) - 0.005
        filter_kwargs["lng__lte"] = float(lng) + 0.005

    paginator = OwnPagination()
    try:
        rooms = Room.objects.filter(**filter_kwargs)
    except ValueError:
        rooms = Room.objects.all()
    results = paginator.paginate_queryset(rooms, request)
    serializer = RoomSerializer(results, many=True)
    return paginator.get_paginated_response(serializer.data)
