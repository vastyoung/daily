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

const 的行为与 let 基本相同，唯一一个重要的区别是用它声明变量时必须同时初始化变量，且尝试修改 const 声明的变量会导致运行时错误。

```javaScript
const age = 26;
age = 36; // TypeError: 给常量赋值

// const 也不允许重复声明
const name = 'Matt';
const name = 'Nicholas'; // SyntaxError
// const 声明的作用域也是块
const name = 'Matt';
if (true) {
    const name = 'Nicholas';
}
console.log(name); // Matt 
```

### 3.4 数据类型

ECMAScript 有 6 种简单数据类型（也称为原始类型）：Undefined、Null、Boolean、Number、String 和 Symbol。Symbol（符号）是 ECMAScript 6 新增的。还有一种复杂数据类型叫 Object（对象）。Object 是一种无序名值对的集合。

```test
"undefined" 表示值未定义；
"boolean"   表示值为布尔值；
"string"    表示值为字符串；
"number"    表示值为数值；
"object"    表示值为对象（而不是函数）或 null；
"function"  表示值为函数；
"symbol"    表示值为符号。
```

```javaScript
//使用 typeof 操作符
let message = "some string";
console.log(typeof message); // "string"
console.log(typeof(message)); // "string"
console.log(typeof 95); // "number" 
```

ECMAScript 提供了 isNaN() 函数.该函数接收一个参数，可以是任意数据类型，然后判断这个参数是否“不是数值”。把一个值传给 isNaN()后，该函数会尝试把它转换为数值。某些非数值的值可以直接转换成数值，如字符串"10"或布尔值。任何不能转换为数值的值都会导致这个函数返回true。

```javaScript
console.log(isNaN(NaN)); // true
console.log(isNaN(10)); // false，10 是数值
console.log(isNaN("10")); // false，可以转换为数值 10
console.log(isNaN("blue")); // true，不可以转换为数值
console.log(isNaN(true)); // false，可以转换为数值 1 
```

#### 3.4.1 数值转换

有 3 个函数可以将非数值转换为数值：Number()、parseInt()和 parseFloat()。Number()是转型函数，可用于任何数据类型。后两个函数主要用于将字符串转换为数值。
