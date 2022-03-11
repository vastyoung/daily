# JavaScript dom

## 第二章 JavaScript语法

```test
通常我们把 JavaScript 代码存为一个扩展名为.js的独立文件，并用他的 src 属性指向该文件，最好的做法是把<script>标签放到 HTML 文档的最后，</body>标签之前.
```

## 第三章 DOM

### 3.1 文档 : DOM 中的 'D'

document(文档) 创建一个网页并把它加载到 Web 浏览器中时，它会把你编写的网页文档转换为一个文档对象.

### 3.2 对象 : DOM 中的 'O'

object(对象).

### 3.3 模型 : DOM 中的 'M'

model(模型) DOM 把一份文档表示为一颗家谱树.

### 3.4 获取元素

#### 3.4.1 getElementById

`getElementById`:这个方法将返回一个与那个有着给定 id 属性值的元素节点对应的对象.

```JavaScript
document.getElementById("id")   //这个 id 值必须放在单引号或者双引号里.
```

#### 3.4.2 getElementsByTagName

`getElementsByTagName` : 这个方法将返回一个对象数组,每个对象分别对应文档里有着给定标签的一个元素.

```JavaScript
document.getElementsByTagName("p")
```

#### 3.4.3 getElementsByClassName

`getElementsByClassName` : 这个方法让我们通过 class 属性中的类名来访问元素.

```JavaScript
document.getElementsByClassName("sale")
```

### 3.5获取和设置属性

#### 3.5.1 getAttribute

`getAttribute` : 这个方法不属于 document 对象,所以不能通过 document 对象调用，只能通过元素节点对象调用.

```JavaScript
var paras = document.getElementsByTagName("p");
for (var i=0; i< paras.length; i++){
   var title_text = paras[i].getAttribute("title");
   if(title_text != null){
    alert(title_text);
   }
}
```

#### 3.5.2 setAttribute

`setAttribute` 这个方法也只能用于元素节点.(它允许我们对属性节点做出修改)

```JavaScript
var shopping = document.getElementById("purchases")
shopping.setAttribute("title","a list of goods")
```

## 第四章 JavaScript图片库

### 4.1 事件处理函数

1. onclick 鼠标点击事件;

2. onmouseover 鼠标悬停在某个元素上触发动作;

3. onmouseout  鼠标指针离开某个元素触发的动作.

```javaScript
//onclick 调用 showPic方法
onclick = "showPic(this);"

//防止用户被带到指定的链接
onclick = "showPic(this); return false;"
```

### 4.2 对这个函数进行拓展

#### 4.2.1 childNodes 属性

childNodes 属性可以用来获取任意一个元素的所有的子元素.(它是一个包含该元素所有子元素的数组)

```javaScript
function countBodyChildren(){
    //获取 body 元素(每份文档只有一个body元素)
    var body_element = document.getElementsByTagName("body")[0];
    //获取 body 元素里面的所有子元素的长度
    alert(body_element.childNodes.length);
    //在加载页面时调用 countBodyChildren
    window.onload = countBodyChildren;
}
```

#### 4.2.2 nodeValue 属性

nodeValue 属性用于得到和设置一个节点的值.

```javaScript
<p id ="description">Choose an image.</p>

var description = document.getElementById("description");
//包含在<p>里的文本是另一种节点,它是<p>标签的第一个子节点 
description.childNodes[0].nodeValue;
```

#### 4.2.3 firstChild 和 lastChild 属性

1. firstChild : 数组的第一个元素;

2. lastChild  : 数组的最后一个元素.

```javaScript
//description.childNodes[0].nodeValue;
description.firstChild.nodeValue;
```

## 第五章 最佳实践

### 5.1 平稳退化

```text
平稳退化 : 让访问者他们的浏览器不支持 javaScript 的情况下仍能够顺利浏览我的网站.(虽然某些功能无法使用，但最基本的操作仍能完成)
```

```javaScript
//javaScript 使用 window 的 open()方法来创建新的浏览器窗口
//window.open(url,name,features) 这3个参数都是可选的
//(1.想在新窗口打开的url;2.新窗口的名字;3.新窗口的尺寸(宽度和高度))
function popUp(winURl){
    window.open(winURL,"popup","width=320,height=480");
}
```

```javaScript
//平稳退化
<a href="http://www.example.com/" onclick="popUp('http://www.example.com/'); return false;">Example</a>

<a href="http://www.example.com/" onclick="popUp(this.getAttribute('href')); return false;">Example</a>

<a href="http://www.example.com/" onclick="popUp(this.href); return false;">Example</a>
```

#### 5.2 向 CSS 学习

##### 5.2.1 结构和样式分离

```test
更推荐的方法先把样式信息存入一个外部文件，再在 head 部分用<link> 标签调用这个文件
```

```css
.warning {
    font-weight: bold;
    color: red
}
```

```html
<p class="warning">
    Be careful!
</p>
```

#### 5.3 压缩脚本

压缩脚本 : 把脚本文件中不必要的字节，如空格和注释，统统删除。

## 第六章 图片库改进版

### 6.1 检查点

我们需要检查当前浏览器是否理解 getElementsByTagName 的 DOM 方法

```javaScript
//如果 getElementsByTagName 未定义 ,就离开
if (!document.getElementsByTagName) return false; 
```

### 6.2 共享 onload 事件

```javaScript
function addloadEvent(func) {
    //把现有的 window.onload 事件处理函数的值存入变量
    var oldonload = window.onload;
    if (typeof window.onload != 'function') {
        //如果这个处理函数还没有绑定任何函数，就像平常那样添加新函数
        window.onload = func；
    } else {
        //如果处理函数已经绑定了一些函数，就把新函数添加到末尾
        window.onload = function() {
        oldonload();
        func();
        }
    }
}
```

## 第七章 动态创建标记

### 7.1 一些传统方法

#### 7.1.1 document.write

document 对象的 write() 方法可以方便把字符串插入到文档.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Test</title>
</head>
<body>
    <script>
        document.write("<p>This is inserted .</p>")
    </script>
</body>
```

## 第八章 充实文档的内容

## 第十章 用 javaScript 实现动画动画效果

