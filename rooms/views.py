from rest_framework.generics import ListAPIView, RetrieveAPIView

from rooms.models import Room
from rooms.serializers import RoomSerializer


class ListRoomsView(ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer
