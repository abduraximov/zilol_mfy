from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("phone", "full_name", "password", "tokens")
        extra_kwargs = {
            "password": {"write_only": True},
            "tokens": {"read_only": True},
        }

    def validate_phone(self, value):
        if User.objects.filter(phone=value).exists():
            raise serializers.ValidationError("This phone number is already in use.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return dict(**validated_data, **tokens)

    def get_tokens(self, obj):
        return dict(refresh=obj["refresh"], access=obj["access"])
