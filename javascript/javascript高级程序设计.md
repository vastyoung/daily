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

## 第五章 基本引用类型

### 5.1 date

```javaScript
//创建 Date 对象
var d = new Date(year, month, day, hours, minutes, seconds, milliseconds);
```

```javaScript
//Date.now() 函数 返回表示方法执行时日期和时间的毫秒数

// 起始时间
let start = Date.now();
// 调用函数
doSomething();
// 结束时间
let stop = Date.now(),
result = stop - start;
```

## 第八章 对象、类与面向对象编程

### 8.1 理解对象

```javaScript
let person = {
    name: "Nicholas",
    age: 29,
    job: "Software Engineer",
    sayName() {
        console.log(this.name);
    }
}; 
```

#### 8.1.1 属性的类型

ECMA-262 使用一些内部特性来描述属性的特征.这些特性是由 JavaScript 实现引擎的规范定义.因此开发者不能再 JavaScript 中直接访问这些特性。为了将某个特性标识为内部特性，规范会用两个中括号把特性包括起来。

属性分两种: 数据属性和访问器属性。

1. 数据属性 :数据属性包含一个保存数据值的位置.值会从这个位置读取,也会写入到这个位置。

    ```text
    [[Configurable]]：表示属性是否可以通过 delete 删除并重新定义,是否可以修改它的特性，以及是否可以把它改为访问器属性。默认情况下，所有直接定义在对象上的属性的这个特性都是 true。

    [[Enumerable]]：表示属性是否可以通过 for-in 循环返回。默认情况下，所有直接定义在对象上的属性的这个特性都是 true。

    [[Writable]]：表示属性的值是否可以被修改。默认情况下，所有直接定义在对象上的属性的这个特性都是 true

    [[Value]]：包含属性实际的值。这就是前面提到的那个读取和写入属性值的位置。这个特性
    的默认值为 undefined。
    ```

    要修改属性的默认特性，就必须使用 Object.defineProperty()方法。这个方法接受3个参数：要给其添加属性的对象、属性的名称和一个描述对象。描述对象上的属性可以包含：configurable、enumerable、writable 和 value。

    ```javaScript
    let person = {};
    Object.defineProperty(person, "name", {
        writable: false,
        value: "Nicholas"
    });
    console.log(person.name); // "Nicholas"
    person.name = "Greg";
    console.log(person.name); // "Nicholas"
    ```

    在调用 Object.defineProperty()时，configurable、enumerable 和 writable 的值如果不指定，则都默认为 false。

2. 访问器属性 ：访问器属性不包含数据值。它们包含一个获取（getter）函数和一个设（setter）函数。

    ```text
    [[Configurable]]：表示属性是否可以通过 delete 删除并重新定义,是否可以修改它的特性，以及是否可以把它改为数据属性。默认情况下，所有直接定义在对象上的属性的这个特性都是 true。

    [[Enumerable]]：表示属性是否可以通过 for-in 循环返回。默认情况下，所有直接定义在对象上的属性的这个特性都是 true。

    [[Get]]: 获取函数，在读取属性时调用。默认值为 undefined。

    [[Set]]；设置函数，在写入属性时调用。默认值为 undefined。
    ```

#### 8.1.2 定义多个属性

在一个对象上同时定义多个属性。ECMAScript 提供了 Object.defineProperties()方法。这个函数接受两个参数：要为之添加或修改属性的对象和另一个描述符对象，其属性与要添加或修改的属性一一对应。

#### 8.1.3 读取属性的特性

使用 Object.getOwnPropertyDescriptor()方法可以取得指定属性的属性描述符。这个方法接受两个参数：属性所在的对象和要取得其描述符的属性名。返回值是一个对象。

ECMAScript 2017 新增了 Object.getOwnPropertyDescriptors()静态方法。这个方法实际上会在每个自有属性上调用 Object.getOwnPropertyDescriptor()并在一个新对象中返回它们。

#### 8.1.4 合并对象

ECMAScript 6 专门为合并对象提供了 Object.assign()方法。这个方法接收一个目标对象和一个
或多个源对象作为参数。

Object.assign()实际上对每个源对象执行的是浅复制。如果多个源对象都有相同的属性，则使
用最后一个复制的值。

#### 8.1.5 对象标识及相等判定

ECMAScript 6 规范新增了 Object.is()，这个方法与===很像。

### 8.2 创建对象

#### 8.2.1 工厂模式

```javaScript
function createPerson(name, age, job) {
    let o = new Object();
    o.name = name;
    o.age = age;
    o.job = job;
    o.sayName = function() {
        console.log(this.name);
    };
    return o;
}
let person1 = createPerson("Nicholas", 29, "Software Engineer");
let person2 = createPerson("Greg", 27, "Doctor");
```

#### 8.2.2 构造函数模式

```javaScript
function Person(name, age, job){
    this.name = name;
    this.age = age;
    this.job = job;
    this.sayName = function() {
        console.log(this.name);
    };
}
let person1 = new Person("Nicholas", 29, "Software Engineer");
let person2 = new Person("Greg", 27, "Doctor");
person1.sayName(); // Nicholas
person2.sayName(); // Greg 
```

按照惯例，构造函数名称的首字母都是要大写的，非构造函数则以小写字母开头。

```javaScript
//构造函数不一定要写成函数声明的形式。赋值给变量的函数表达式也可以表示构造函数：
let Person = function(name, age, job) {
    this.name = name;
    this.age = age;
    this.job = job;
    this.sayName = function() {
        console.log(this.name);
    };
}
let person1 = new Person("Nicholas", 29, "Software Engineer");
let person2 = new Person("Greg", 27, "Doctor");
person1.sayName(); // Nicholas
person2.sayName(); // Greg
console.log(person1 instanceof Object); // true
console.log(person1 instanceof Person); // true
console.log(person2 instanceof Object); // true
console.log(person2 instanceof Person); // true 
```
