from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from django.views import View
def index(request):
    return HttpResponse("Hello, world. You're at the course index. ")

def auth(request):
    return JsonResponse({'status':True, 'message':'success'})

class UserView(View):
    def get(self, request):
        return JsonResponse({'status':True,'message':'success'})

    def post(self, request):
            pass