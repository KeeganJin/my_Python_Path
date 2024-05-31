# Introduction
This is a Django rest framework tutorial, which covers the most straightforward use, including:
* Auth
* Permissions
* Throttle
* Version
* Parser
* Serialization
# What is a REST API?

## My learning material

[Django Restful Framework Tutorial](https://www.bilibili.com/video/BV1Dm4y1c7QQ/?p=2&spm_id_from=pageDriver&vd_source=6fc8e1c6291daeac135f1f6a0c223395)

* Representational State Transfer
* All about communication

# Example
* The request send to the server
* the response send back from server to client

## CRUD
* Create - Post
* read - get
* update - put
* delete - delete



## Basics

  ### 前后端分离
  * 后端向前端 XML, JSON 传输数据
  * 后端按照约定的数据格式向前端提供接口
  ### Some Django and Python Basics

  * OOP
    * 封装
      * 将对同一类方法封装到类中
      ```python
      Class File:
        CRUD
      Class DB:
        DB Operation methods
       ```
       *将数据封装到对象中
       ```python
       class File:
          def __init__(self,a1,a2):
            self.a1 = a1,
            self.a2 = a2
          def get:..
       ```
## FBV & CBV
the difference is based on function or based on class.
```python

urlpatterns = [

  path('user/',view.UserView.as_view())
]


class UserView(View):
  def get(self,request):
    return JsonResponse(..)
  def post(self,request):
    pass

class InfoView(APIView):

```
## DRF -> CBV
View
APIView(View)
## CBV -> (drf) -> dispatch
* the request object of Django
  * request.method
  * request.GET
  * request.POST
  * etc.
* the request object of drf
```python
class Request:
  def __init__(self,request,....):
    self._request = request
    .. 
```

## OOP

### Request object
* __getattr__: access the unexited method through the object will triger it.
* __getattribute__:   

## Auth
### How to use
* create Authentication class
* create class variable within Userview class
* add required authentication to Userview
```python
class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # User auth:
        # 1. read token from request
        # 2. verify legal
        # 3. return value
        token = request.query_params.get('token')
        if token:
            return 'King', token
        raise AuthenticationFailed("Invalid token")

class LoginView(APIView):
    authentication_classes = []
    def get(self, request):
        return Response({"message": "Hello World!"})
class UserView(APIView):

    authentication_classes = [MyAuthentication,]
    def get(self,request,format=None):
        return Response({"message":"Hello from UserView!"})


class OrderView(APIView):
    authentication_classes = [MyAuthentication,]
    def get(self,request,format=None):
        return Response({"message":"Hello from OrderView!"})
```

### Global default setting
when there are too many views need authentication, use default authentication.
```python
# within the settings.py
REST_FRAMEWORK={
  'DEFAULT_AUTHENTICATION_CLASSES':["XXX.XX.MyAuthentication".]
}
```
### Application: User Login

#### return e.g, uuid token to stay user login.
token can be stored in cookies. in the following example, we use url to pass the token. 
* login to generate token.
* user end save token, if token authtication pass, then access userview
```python
import uuid

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from api import models
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello World!</h1>")

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
    authentication_classes = [QueryParamsAuthentication,]
    def get(self,request,format=None):
        return Response({"message":"Hello from OrderView!"})
```

## Permissions
* the excution order is authentication first, then permision in the source code
* The Permission can be set as AND mode/ OR mode
* Permission is after Authentication, therefore, request has the user.
```python
from  rest_framework.permissions import BasePermission
class UserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 3:
            return True
        return False

class ManagerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role ==2:
            return True
        return False

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role ==1:
            return True
        return False

class OrderView(APIView):
    authentication_classes = [QueryParamsAuthentication]
    permission_classes = [UserPermission]
    def get(self,request):
        print(request.user,request.auth)
        return Response({"message":"Hello from OrderView!"})
```
## Throttle
* E.g, according to IP, limit user usage of the API
* Find the unique ID to limit usage
  * user name, IP, 
  
