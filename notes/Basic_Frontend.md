# Frontend

## HTML

HTML + FLASK

[Tutorial](https://www.runoob.com/html/html-tutorial.html)

**Form** is used to **submit** messages

* action, method...

**GET**, **POST**

## CSS

* **style tag**

* store in a .css file
* 类选择器 **.c1**, ID 选择器**#c2**， 标签选择器 e.g. **div{}**

#### BootStrap



## JavaScript

#### 1 Basics

**DOM(document)** **BOM**

```html
<script> </script>
```

**代码位置**

*  head 标签里面，放在末尾

* body 标签里面的尾部（一般放在这里）

**存在形式**

* 写在文件里，导入文件

   ```html
  <script src="static/my.js"></script>
   ```

* ```html
  <script type="text/javascript"></script>
  ```

JavaScript Basics

```javascript
var name = "King";
```

``` javascript
var v1 = name.length;
```

A sample of using JS: 跑马灯

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Temp</title>
</head>
<body>

    <span id="txt">Welcome to my website </span>

    <script type="text/javascript">
        function show(){
            var tag = document.getElementById("txt");
            var dataString = tag.innerText;

            var firstChar = dataString[0];
            var otherString = dataString.substring(1,dataString.length);
            var newText = otherString + firstChar;

            //update content in HTML tag
            tag.innerText = newText;

            // console.log(dataString);
        }

        //timer
        setInterval(show,1000);
    </script>
</body>
</html>
```

**JS array** 

```javascript
var v1 = [1,2,3,4];
var v2 = Array([12,34,4]);
```

​	array manupilation

```javascript
v1[1] = 12;
v1.push("hello");
v1.unshift("hello");
v1.splice(1,0,"hello");//(index, 0, "element")
v1.pop();//尾部删除
v1.shift();头部删除
v1.splice(index,1);//删除特定
```

```javascript
var v1 = [1,2,3,4];
for(var idx in v1){
    //循环的是索引
}
for(var i=0; i<v1.length; i++){
    
}
```

Dynamically add content to HTML

```html
    <ul id="city">
    </ul>
    <script type="text/javascript">
        var cityList = ["Beijing","Shanghai","ShenZhen"];
        for(var idx in cityList){
            var text = cityList[idx];

            //create <li>
            var tag = document.createElement("li");
            tag.innerText = text;

            //add to id=city, DOM
            var parentTag = document.getElementById("city");
            parentTag.appendChild(tag);

        }
    </script>
```



#### **2. DOM**

```javascript
//get tag according to ID
var tag = document.getElementById("");
//have the content fo a tag
tag.innerText;
//change the content of a tag
tag.innerText = "Hey hey";

//create a tag
var tag = document.createElement("div");
```

```html
//add new tag inside of another tag
 <ul id="city">    </ul>

<script type="text/javascript">
    //add to id=city, DOM
    var parentTag = document.getElementById("city");
    var newTag = document.createElement("li");
    tag.innerText = "Beijing";
    
    parentTag.appendChild(newTag);
    
</script>
```

##### 2.1 事件绑定

绑定onclick（）

```html
<span id="txt">Welcome to my website </span>

<input type="button" value="click to loop" onclick="show()">
<script type="text/javascript">
    function show(){
        var tag = document.getElementById("txt");
        var dataString = tag.innerText;

        var firstChar = dataString[0];
        var otherString = dataString.substring(1,dataString.length);
        var newText = otherString + firstChar;

        //update content in HTML tag
        tag.innerText = newText;
        console.log(dataString);
    }

    //timer
    // setInterval(show,1000);
</script>
```

#### 3. Summary

Dom可以实现，但是代码量大，理解即可。实际生产中，JQuery或者一系列其它的工具。



## 4. JQuery

### 4.1 快速上手

```html
<h1 id="txt_1">German Telkom</h1>
<!--    Using JQuery, it makes the process simple-->

<script src="static/jquery-3.7.1.min.js"></script>
<script type="text/javascript">
    $("#txt_1").text("it Sucks");
</script>
```



### 4.2 Search Tag

* By ID

```html
<h1 id="txt_1">German Telkom</h1>
<script type="text/javascript">
    $("#txt_1").text("it Sucks");
</script>
```

* By Class 样式选择器，类选择器

```html
<h1 class="c1">Basketball 1</h1>
<h2 class="c1">Basketball 1</h2>
<h3 class="c1">Basketball 1</h3>

<script type="text/javascript">
    $(".c1");
</script>
```

* By Tag

```html
<h1 class="c1">Basketball 1</h1>
<h2 class="c1">Basketball 1</h2>
<h3 class="c1">Basketball 1</h3>

<script type="text/javascript">
    $("h1");
</script>
```

* 层级选择器

```html
<h1 class="c1">
	<h2 class="c2">Basketball 1</h2>
</h1>

<script type="text/javascript">
    $(".c1 .c2");
</script>
```

* 多选择器

```html
$("#c1,#c2,li")
```

* 属性选择器

```html
<input type='text' name="n1"/>
```

```html
$("input(name='n1')")
```

### 4.3 Indirectly Search

* Find siblings

```html
<div>
    <div>Bejing</div>
    <div>Bejing</div>
	<div>Bejing</div>
</div>
```

* Find Parent/ Children

```html
$("#c1").parent().children()
```

### 4.4 Example: Menu Switch（样式操控 Class） 

其中主要使用的是addClass，removeClass

```html

<body>
    <div class="menus">
        <div class="item">
            <div class="header" onclick="clickMe(this);">Beijing</div>
            <div class="content hide">
                <a>bejing 1</a>
                <a>bejing 2</a>
            </div>
        </div>

        <div class="item">
            <div class="header">Shanghai</div>
            <div class="content hide">
                <a>Shanghai 1</a>
                <a>Shanghai 2</a>
            </div>

        </div>
    </div>

    <script src="static/jquery-3.7.1.min.js"></script>

    <script>
        function clickMe(self){

            //find the silbings tag
            var hasHide = $(self).next().hasClass("hide");

            if (hasHide){
                //remove class "hide"
                $(self).next().removeClass("hide");
            } else {
                $(self).next().addClass("hide");
            }


        }
    </script>
```

### 4.5  值的操控

```html
<div id='c1'>
    content
</div>
```

```javascript
$("#c1").text("new content")
```

```html
<input type='text' id ='c2'/>
```

```javascript
$('#c2').val()// get the user input
```

### 4.6 绑定事件

通过JQuery实现

```javascript
$("li").click(function()){
              $(this).remove();
              }
```

当页面框架加载结束后，自动执行

使用这种写法，更加快速

```javascript
$(function()){
  //当页面框架加载完成后，自动执行
  $("li").click(function()){
                ...
                }
  }
```

### 4.7 Table

## 5 Summary of Frontend

