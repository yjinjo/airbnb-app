from rest_framework import serializers

from users.models import User


class RelatedUserSerializer(serializers.ModelSerializer):
    """다른 유저의 정보 Detail"""

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "superhost",
        )


class ReadUserSerializer(serializers.ModelSerializer):
    """내 정보에 대한 Detail"""

    class Meta:
        model = User
        exclude = (
            "groups",
            "user_permissions",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        )


class WriteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )
