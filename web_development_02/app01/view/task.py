from django.http import HttpResponse
from django.shortcuts import render,redirect
from app01 import models

def task_list(request):
    return render(request,"task_list.html")


def task_ajax(request):
    print(request.GET)
    return HttpResponse("Success")