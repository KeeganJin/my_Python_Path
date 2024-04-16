from django.shortcuts import render, redirect
from app_01 import models
from django import forms


# Create your views here.
def department_list(request):
    '''
    get data of department from the database
    and return the queryset to the html file, so that JS code in the
    html file can render properly
    '''
    queryset = models.Department.objects.all()

    return render(request, 'department_list.html', {'department_queryset': queryset})


def new_department(request):
    pass


def test(request):
    return render(request, 'test.html')


def department_add(request):
    if request.method == 'GET':
        return render(request, 'department_add.html')
    if request.method == 'POST':
        # get the data from form
        department_name = request.POST.get('department_name')
        # operate on the database
        models.Department.objects.create(title=department_name)
        return redirect("/department/list/")


def department_delete(request):
    # use n_id as the name of argument
    nid = request.GET.get('n_id')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/department/list/")


def department_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        # send data from backend to frontend
        return render(request, 'department_edit.html', {"row_object": row_object})
    title = request.POST.get('department_name')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/department/list/")


def user_list(request):
    queryset = models.UserInfo.objects.all()

    return render(request, 'user_list.html', {"user_queryset": queryset})


# def user_add(request):
#     '''get data from models and add to the front page
#     based on normal methods
#     '''
#     if request.method == 'GET':
#         context = {
#             'gender_choices': models.UserInfo.gender_choices,
#             'department_choices': models.Department.objects.all()
#         }
#         # context here is dict
#         return render(request, 'user_add.html',context)
#     if request.method == 'POST':
#         # get the data from form
#         user_name = request.POST.get('user_name')
#         # operate on the database
#         models.UserInfo.objects.create(name=user_name)
#         return redirect("/user/list/")

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time',
                  'department', 'gender']
        '''control the frontend page properties from backend'''

        # add widget one by one
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form"}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#             find all fields and add class = "form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

def user_add(request):
    '''based on ModelForm method'''
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    else:
        return render(request,"user_add.html",{'form':form})

def user_edit(request, nid):

    if request.method == 'GET':
        row_object = models.UserInfo.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        # send data from backend to frontend
        return render(request, 'user_edit.html', {"form": form})

    # get form data from the POST request
    row_object = models.UserInfo.objects.filter(id=nid).first()

    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    else:
        return render(request, "user_add.html", {'form': form})

def user_delete(request):
    # use n_id as the name of argument
    nid = request.GET.get('n_id')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")




from django.core.paginator import Paginator
def fancy_num_list(request):
    data_dict = {}

    filter = request.GET.get('filter')

    if filter:
        queryset = models.FancyNum.objects.filter(mobile__contains=filter)
        return render(request, 'fancy_number_list.html', {"fancy_queryset": queryset,"filter":filter})

    queryset = models.FancyNum.objects.all().order_by("-level")
    paginator = Paginator(queryset,10)
    return render(request,'fancy_number_list.html',{"fancy_queryset": queryset,"filter":filter})

class FancyNumModelForm(forms.ModelForm):
    class Meta:
        model = models.FancyNum
        fields = ['mobile', 'price', 'level', 'status']

        # add widget one by one
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form"}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
#             find all fields and add class = "form-control"
        for name, field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

def fancy_num_add(request):
    '''based on ModelForm method'''

    if request.method == 'GET':
        form = FancyNumModelForm()
        return render(request, 'fancy_num_add.html', {'form': form})

    form = FancyNumModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/fancy/list")
    else:
        return render(request,"fancy_num_add.html",{'form':form})


def fancy_num_edit(request, nid):

    if request.method == 'GET':
        row_object = models.FancyNum.objects.filter(id=nid).first()
        form = UserModelForm(instance=row_object)
        # send data from backend to frontend
        return render(request, 'fancy_num_edit.html', {"form": form})

    # get form data from the POST request
    row_object = models.FancyNum.objects.filter(id=nid).first()

    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/fancy/list")
    else:
        return render(request, "fancy_num_edit.html", {'form': form})

def fancy_num_delete(request):
    pass