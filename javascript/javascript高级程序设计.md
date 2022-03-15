# JavaScript高级程序设计

## 第一章 什么是 JavaScript

JavaScript 是一门用来与网页交互的脚本语言，它包含三个部分：

1. ECMAScript ：由 ECMA-262 定义并提供核心功能。

2. 文档对象模型（DOM）：提供与网页内容交互的方法和接口。

3. 浏览器对象模型（BOM）：提供与浏览器交互的方法和接口。

## 第二章 HTML 中的 JavaScript

```test
JavaScript 是通过<script>元素插入到 HTML 页面中的。这个元素可用于把 JavaScript 代码嵌入到HTML 页面中，跟其他标记混合在一起，也可用于引入保存在外部文件中的 JavaScript.
```

要使用外部的 JavaScript 文件，必须将 src 属性设置为要包含文件的 URL。

## 第三章 语言基础

### 3.1 变量

#### 3.3.1 var 关键字

```javaScript
//使用 var 在一个函数内部定义一个变量,就意味该变量在函数退出是被销毁.
function test() {
    var message = "hi"; //局部变量
}
test();
console.log(message); //出错
```

```javaScript
function test() {
    message = "hi"; // 全局变量
}
test();
console.log(message); // "hi"
```

#### 3.3.2  var 声明提升

使用 var 这个关键字声明的变量会自动提升到函数作用域顶部.

```javaScript
function foo(){
    console.log(age);
    var age = 26;
}
foo(); // undefined
```

```javaScript
function foo() {
    var age = 16;
    var age = 26;
    var age = 36;
    console.log(age);
}
foo(); // 36 
```

#### 3.3.3 let 声明

let 跟 var 的作用差不多，但有着非常重要的区别。最明显的区别是，let 声明的范围是块作用域，而 var 声明的范围是函数作用域。

```javaScript
if (true) {
    var name = 'Matt';
    console.log(name); // Matt
}
console.log(name); // Matt
```

```javaScript
if (true) {
    let age = 26;
    console.log(age); // 26
}
console.log(age); // ReferenceError: age 没有定义
```

```javaScript
//嵌套使用相同的标识符不会报错,因为同一个块中没有重复.
var name = 'Nicholas';
console.log(name); //'Nicholas'

if(true)(
    var name = 'Matt';
    console.log(name); //'Matt'
)

let age = 30;
console.log(age); // 30

if (true) {
    let age = 26;
    console.log(age); // 26
} 
```

#### 3.3.4 const 声明
