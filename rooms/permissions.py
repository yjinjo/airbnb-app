from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, room):
        """
        :param room: obj --> room
        """
        return room.user == request.user
