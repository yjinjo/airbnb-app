from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "superhost",
            "password",
        )
        read_only_fields = ("id", "superhost", "avatar")

    def validate_first_name(self, value):
        return value.upper()

    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data.get("password")
        user.set_password(password)
        user.save()
        return user
