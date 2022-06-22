import rest_framework.views
from rest_framework.views import APIView

from custom_auth.serializers import *
from custom_auth.models import CustomUser
from custom_auth.helpers import encrypt, encode_jwt, decode_jwt

from rest_framework.views import Response


class RegisterAuthAPI(APIView):

    # Register a new User
    def post(self, request):
        newUser = NewUserSerializer(data=request.data)
        newUser.is_valid(raise_exception=True)

        user = CustomUser(**newUser.validated_data)

        user.save()

        return Response(data="Created")


class LoginAuthAPI(APIView):

    # Login with an existing user
    def post(self, request):
        newUser = LoginSerializer(data=request.data)
        newUser.is_valid(raise_exception=True)

        username = newUser.validated_data.get("username")
        password = encrypt(newUser.validated_data.get("password"))

        user = CustomUser.objects.filter(username=username, password=password)

        is_creditentials_correct = user.count() > 0

        if is_creditentials_correct:
            return Response(data=encode_jwt(username))

        return Response(data="Login Failed", status=400)
