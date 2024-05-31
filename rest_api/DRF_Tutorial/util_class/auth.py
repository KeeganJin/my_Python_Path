from api import models
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

class QueryParamsAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # User auth:
        # 1. read token from request
        # 2. verify legal
        # 3. return value
        token = request.query_params.get('token')
        if not token:
            return
        user_object = models.User.objects.filter(token=token).first()
        # if not user_object:
        #     return Response({"message":"pls login"})
        if user_object:
            print("user object found")
            return user_object, token

        return

    def authenticate_header(self, request):
        return 'API'

class HeaderParamsAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return
        user_object = models.User.objects.filter(token=token).first()
        if user_object:
            return user_object, token
        return

    def authenticate_header(self, request):
        return 'API'

class NoAuthTokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        raise AuthenticationFailed({"status":False, "message":"invalid"})
    def authenticate_header(self, request):
        return 'API'