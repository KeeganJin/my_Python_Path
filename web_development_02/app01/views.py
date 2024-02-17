from django.http import HttpResponse
from django.shortcuts import render,redirect
from app01 import models
# Create your views here.

def depart_list(request):

    # get result from departments
    # 在后端循环没有意义，将结果交给前端
    queryset = models.Department.objects.all()

    return render(request,"depart_list.html",{'queryset':queryset})

def depart_add(request):
    if request.method == "GET":
        return render(request, "depart_add.html")
    title = request.POST.get("title")
    
    # save to database
    models.Department.objects.create(title=title)

    #redirect to department list
    return redirect("/depart/list/")

def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")

def depart_edit(request,nid):
    # get data according to nid
    if request.method=="GET":

        row_object = models.Department.objects.filter(id=nid).first()
        print(row_object.id, row_object.title)

        return render(request,"depart_edit.html",{'row_object':row_object})
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")

def user_list(request):
    queryset = models.UserInfo.objects.all()
    return render(request,'user_list.html',{'queryset':queryset})