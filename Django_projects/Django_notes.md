# Django
[ref link](https://github.com/jackfrued/Python-100-Days/blob/master/Day41-55/41.Django%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B.md)

## Installation. 
Using Anaconda

## The framework

MVC
* model
* controller
* view

### Files within a django project

#### within the main folder
* hellodjango/__init__.py：空文件，告诉Python解释器这个目录应该被视为一个Python的包。
* hellodjango/settings.py：Django项目的配置文件。
* hellodjango/urls.py：Django项目的URL映射声明，就像是网站的“目录”。
* hellodjango/wsgi.py：项目运行在WSGI兼容Web服务器上的入口文件。
* manage.py： 管理Django项目的脚本程序。
* 说明：WSGI全称是Web服务器网关接口，维基百科上给出的解释是“为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口”。
#### within the application folder
* __init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
* admin.py：可以用来注册模型，用于在Django框架自带的管理后台中管理模型。
* apps.py：当前应用的配置文件。
* migrations：存放与模型有关的数据库迁移信息。
* __init__.py：一个空文件，告诉Python解释器这个目录应该被视为一个Python的包。
* models.py：存放应用的数据模型（MTV中的M）。
* tests.py：包含测试应用各项功能的测试类和测试函数。
* views.py：处理用户HTTP请求并返回HTTP响应的函数或类（MTV中的V）。

### vitural environment

* create new environemnt, isolate python packages

## Javascript + DOM (Document object model)

### Example: Array
append list to html
```html
<ul id="city"></ul>
<script>
    var cityList = ["beijing","shanghai","shenzhen"];
    for (var idx in cityList){
        var text = cityList[idx];

        var tag = document.createElement("li");
        tag.innerText = text;

        var parentTag = document.getElementById("city");
        parentTag.appendChild(tag);
</script>
```
### Object, dictionary of python
```html
```
### DOM

#### get user input
```html
var text=document.getElementById('input1').value;
```

## jQuery

A simple fast way to achieve same thing using DOM
get content, set content. 


## ORM

## Model Form

* create a class of the form/table
* use it.
* it can be re-used many times, check the fancy_num and user of the management sys project.

### Filter

```python
models.UserInfo.objects.filter(name = "lu",id=12)
dict = {"name":lu,id:12}
models.UserInfo.objects.filter(**dict)


models.UserInfo.objects.filter(id=12)
models.UserInfo.objects.filter(name__startswith="xx")
models.UserInfo.objects.filter(name__contains="xx")
```
pass the arguments from front to the end by name.
```html
<form method="get" class="d-flex" role="search">
    <input name="filter" class="form-control me-2" type="search" placeholder="Filter" value="{{ filter }}"  aria-label="Search">
    <button class="btn btn-outline-success" type="submit">Search</button>
</form>
```
```python
def fancy_num_list(request):
    data_dict = {}

    filter = request.GET.get('filter')

    if filter:
        queryset = models.FancyNum.objects.filter(mobile__contains=filter)
        return render(request, 'fancy_number_list.html', {"fancy_queryset": queryset,"filter":filter})

    queryset = models.FancyNum.objects.all().order_by("-level")
    return render(request,'fancy_number_list.html',{"fancy_queryset": queryset,"filter":filter})

```

## Pagination 
not done yet, can refer to django pagination

## Cookie and Session
* 短链接： 一次请求， 一次响应。
* 




