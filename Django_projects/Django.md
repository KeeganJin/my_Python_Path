# Django



## 1 ORM + MySQL



### 1.1 Table Design

```python
class Department(models.Model):
    """Department Table"""
    title = models.CharField(verbose_name="Department Title", max_length=32)

class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(max_digits=18,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="enroll time")
#django auto add _id, so it will be depart_id
    depart = models.ForeignKey(to="Department", to_field="id",on_delete=models.CASCADE)
    
    gender_choices = (
        (1, "male"),
        (0, "female"),
    )
    gender = models.SmallIntegerField(verbose_name="gender",choices=gender_choices)

```

* foreign table constraint
  * 只能是部门表中已存在的ID
* delete related tables
  * also delete user, 级联删除
  * the depart ID set to Null

### 1.2 Table Generate

* create database

```
create database dj_learn DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

* modify **settings.py** to connect database

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        'NAME': 'unicom',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```

* create DB table by using django commands

```
python manage.py makemigrations
python manage.py migrate
```

## 2. Get on Hand

* **urls.py**

```python
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('depart/list/', views.depart_list)
]
```

* **views.py**

```python
def depart_list(request):

    # get result from departments
    # 在后端循环没有意义，将结果交给前端
    queryset = models.Department.objects.all()
    return render(request,"depart_list.html",{'queryset':queryset})
```

* **templates/depart_list.html**

将queryset交给前端

```html
{% for obj in queryset %}
<tr>
    <td>{{ obj.id }}</td>
    <td>{{ obj.title }}</td>
    <td>
        <a class="btn btn-primary" href="">Modify</a>
        <a class="btn btn-primary" href="">Delete</a>
    </td>
</tr>
{% endfor %}

```



### 2.1 Delete

get content from GET Request 

```python
def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")
```

```html
<a class="btn btn-primary" href="/depart/delete/?nid={{ obj.id }}">Delete</a>
```

### 2.2.Template inherit

```html
{% block content %}
{% endblock %}
```

inherit the template by doing

```html
{% extends 'layout.html' %}
{% block content %}
new content
{% endblock %}
```

### 2.3 Django 内联table

```python
class Department(models.Model):
    """Department Table"""
    title = models.CharField(verbose_name="Department Title", max_length=32)

class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    account = models.DecimalField(max_digits=18,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="enroll time")

    # Django中的约束
    gender_choices = (
        (1, "male"),
        (0, "female"),
    )
    gender = models.SmallIntegerField(verbose_name="gender",choices=gender_choices)

    depart = models.ForeignKey(to="Department", to_field="id",on_delete=models.CASCADE)
```

**Django 在db中生成的depart的列为depart_id**,在获取到userInfo后可以通过depart获得相关联的表

```python
obj.depart.title
```



## 3.Form, ModelForm

[modelform tutorial](https://www.bilibili.com/video/BV1rT4y1v7uQ?p=63&spm_id_from=pageDriver&vd_source=6fc8e1c6291daeac135f1f6a0c223395)