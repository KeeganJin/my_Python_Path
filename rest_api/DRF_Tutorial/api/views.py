import uuid

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
from util_class.auth import QueryParamsAuthentication,HeaderParamsAuthentication, NoAuthTokenAuthentication
from util_class.per import UserPermission,ManagerPermission,AdminPermission

# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World!</h1>")
class LoginView(APIView):
    authentication_classes = []
    def get(self, request):
        return Response({"message": "Hello World!"})
    def post(self, request):
        # 1. get user data from post request
        print(request.data)
        print(request.query_params)
        username = request.data.get('username')
        password = request.data.get('password')

        # 2. verify from database
        user_object = models.User.objects.filter(username=username).first()
        if not user_object:
            return Response({"code":101,"message":"Invalid"})

        # 3. if correct
        token = str(uuid.uuid4())
        user_object.token = token
        user_object.save()
        return Response({"status":True,'data':token})

class UserView(APIView):

    authentication_classes = [QueryParamsAuthentication,HeaderParamsAuthentication,NoAuthTokenAuthentication]
    def get(self,request,format=None):
        return Response({"message": "Hello from UserView!"})


class OrderView(APIView):
    authentication_classes = [QueryParamsAuthentication]
    permission_classes = [UserPermission]
    def get(self,request):
        print(request.user,request.auth)
        return Response({"message":"Hello from OrderView!"})