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

## Database
pymysql
```python

#Connect to the database
connection = pymysql.conncect()


```

## ORM
* operate on tables in database
* operate on data

Object class in models represent table
```python
class UserInfo(models.Model):
    name = models.CharField(max_length =32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
# is equal to sql query, app01 is the app name
"""
create table app01_userinfo(
    id bigint auto_increment primary key,
    name varchar(32),
    password varchar(64),
    age int
)
"""
```





