from rest_framework import serializers
from custom_auth.models import CustomUser


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "username", "password"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=64)
    password = serializers.CharField(min_length=3, max_length=64)

