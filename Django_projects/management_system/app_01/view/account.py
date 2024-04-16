from django.shortcuts import render, redirect
from app_01 import models
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")


def login(request):

    if request.method == 'GET':

        form = LoginForm()
        return render(request,'login.html',{'form':form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        return redirect(request,'login.html',{'form':form})