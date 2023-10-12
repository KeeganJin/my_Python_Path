from django.shortcuts import render,HttpResponse

# Create your views here.
# default argument request
def index(request):
    return HttpResponse("666")



def tpl(request):
    name = "king"
    roles=["liu","guan","zhang"]

    return render(request,'tpl.html',{"n1":name, "n2":roles})

def test(request):
    # request is a object
    pass

def login(request):
    if(request.method=="GET"):
        return render(request,'login.html')
    else:
        print(request.POST)
        return HttpResponse("Success")

from app01.models import UserInfo
def user_list(request):
    data_list = UserInfo.objects.all()
    for item in data_list:
            print(data_list)
    return render(request,"user_list.html")

def user_add(request):
    if request.method == "GET":
        return render(request,"user_add.html")
    # get the user submitted data
    user = request.POST.get("username")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")

#    add to database
    UserInfo.objects.create(name=user,password=pwd,age=age)
    return HttpResponse("success")