from rest_framework.decorators import api_view
from rest_framework.response import Response

from rooms.models import Room
from rooms.serializers import RoomSerializer


@api_view(["GET"])
def list_rooms(request):
    rooms = Room.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)
