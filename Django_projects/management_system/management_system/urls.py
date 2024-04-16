"""
URL configuration for management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_01 import views
from app_01.view import account

urlpatterns = [
    path('admin/', admin.site.urls),

    # department management
    path('department/list/', views.department_list),
    path('test/', views.test),
    path('department/add/',views.department_add),
    path('department/delete/',views.department_delete),
    path('department/<int:nid>/edit/',views.department_edit),

    # user management
    path('user/list/', views.user_list),
    path('user/add/',views.user_add),
    path('user/<int:nid>/edit/',views.user_edit),
    path('user/delete/',views.user_delete),


    path('fancy/list/',views.fancy_num_list),
    path('fancy/add/',views.fancy_num_add),
    path('fancy/delete/',views.fancy_num_delete),
    path('fancy/<int:nid>/edit/',views.fancy_num_edit),

    path('login/',account.login)
]
