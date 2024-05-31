
## Django framework
### underneath logic
url -> app.views -> app.views ->app.templates

## 1 Preparation

* create & register app
  ```python
  
  ```
* create table.
### Table Operation
#### constrains, cascade, set_null
```python
class Department(models.Model):
    title = models.CharField(verbose_name='Title',max_length=32)

class UserInfo(models.Model):
    name = models.CharField(verbose_name='Name',max_length=32)
    password = models.CharField(verbose_name='Password',max_length=64)
    age = models.IntegerField(verbose_name='Age')
    account = models.DecimalField(verbose_name='Age',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name='start_time')

    # with constraints,
    # to indicate which table,
    depart = models.ForeignKey(to='Department', to_field='department', to_fields='id')

```
#### Database Operations
1. create database
```mysql
create database management_sys default charset utf8 collate utf8_general_ci;
```
2. set the setting config file, connect to MySQL
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'management_sys',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
3. use django command to create table
```
makemigrations
migrate
```

### Static files managements
static and templates
within the app folder

### Add bootstrap and jquery

[A quick start of bootstrap and javascript](https://getbootstrap.com/docs/4.3/getting-started/introduction/#quick-start)

* bootstrap in head
* Place Jquery the following scripts near the end of your pages, right before the closing body tag

## 2. Frontend part 
### Template Inherit

**layout.html**

```html
<div>
    <div class="container">
        {% block content %} {% endblock %}
    </div>

</div>
```

```html
{%  extends 'layout.html' %}

{% block content %}

    
    
{% endblock %}
```

## 3 Data Operation

access data via views 

**Example**
```python
# views.py in the app 
# it return the html file rendered by given queryset
def department_list(request):

    '''
    get data of department from the database
    and return the queryset to the html file, so that JS code in the
    html file can render properly
    '''
    queryset = models.Department.objects.all()

    return render(request, 'department_list.html', {'department_queryset': queryset})

```
```html
<!-- the query set is given to the html file -->
<tbody>
{% for obj in department_queryset %}
    <tr>
        <th>{{ obj.id }}</th>
        <td>{{ obj.title }}</td>
        <td>
            <a class="btn btn-primary" href="#">Modify</a>
            <a class="btn btn-danger" href="#">Delete</a>

        </td>
    </tr>
{% endfor %}
</tbody>
```

### Input
* "name": As for the name, that is used to identify the user input in the POSTDATA on Submit.
* "id" : The id could be a hook for some CSS selector rule, it could be a hook for a JS element node to capture events, or it could be associated with a label.

### CRUD
```python
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

def department_edit(request,nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        # send data from backend to frontend
        return render(request, 'department_edit.html', {"row_object": row_object})
    title = request.POST.get('department_name')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/department/list/")
```

### Foreign table
```python
'''
user_obj.department is the corresponding row of the department table, 
then user_obj.department.title will be the corresponding department title
'''
class Department(models.Model)
    title = ..
class UserInfo(models.Model):
   department = models.ForeignKey(to='Department', to_field='id',on_delete=models.CASCADE)


```

Check, Error, more convinient

### Form
## ModelForm (CRUD for DB)
widget 可以加在views中

###
