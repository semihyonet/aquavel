from custom_auth.models import CustomUser
from django.http import HttpRequest
from custom_auth.helpers import decode_jwt

class AuthJTWDecode:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request:HttpRequest ):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        auth_header = request.headers.get("Authorization", "")


        print("sadas",auth_header)

        if auth_header == "" or len(auth_header) < 8 or auth_header[0:6] != "Bearer":
            request.user = None




        else:
            jwt_token = auth_header[7:]
            username = decode_jwt(jwt_token).get("user_id")


            if CustomUser.objects.filter(username=username).count() > 0:
                request.user = CustomUser.objects.get(username=username)
                print(request.user)

            else:
                request.user = None


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
