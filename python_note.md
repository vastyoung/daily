# python

在你的操作系统中开启终端程序然后通过输入python并按下回车键来打开 Python 提示符

`print("Hello World")` :打印 Hello World

退出解释器环境可以通过按下 [ctrl + d] 组合键或是输入 exit() （注意：要记住要包含括号 ()）并敲下回车实现

`python hello.py` :运行 hello.py 程序

`help('len')` :显示出有关 len 函数的帮助

## 注释

`print('hello world')` #注意 print 是一个函数

```python
# 注意 print 是一个函数
print('hello world')

```

## 变量

命名需要遵守以下规则：

第一个字符必须是字母表中的字母（大写 ASCII 字符或小写 ASCII 字符或 Unicode 字符）或下划线（_）。

其它部分可以由字符（大写 ASCII 字符或小写 ASCII 字符或 Unicode 字符）、下划线（_）、数字（0~9）组成。

名称区分大小写。例如，myname 和 myName 并不等同。要注意到前者是小写字母 n 而后者是大写字母 N。

有效 的名称可以是 i 或 name_2_3 ，而 2things，this is spaced out，my-name 或 >a1b2_c3都是无效 的名称。

```python
#从其他信息中构建字符串。这正是 format() 方法
#str_format.py
age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
```

`python str_format.py` :Swaroop was 20 years old when he wrote this book
                        Why is Swaroop playing with that python?

```python
#数字只是一个可选选项
age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
```

```python
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'  
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
```

注意 print 总是会以一个不可见的“新一行”字符（\n）结尾，因此重复调用 print将会在相互独立的一行中分别打印。为防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾

```python
print('a', end='')
print('b', end='')#输出ab
```

通过 end 指定以空格结尾

```python
print('a', end=' ')
print('b', end=' ')
print('c')          #输出a b c
```

## 转义序列

如果你希望生成一串包含单引号（'）的字符串，你应该如何指定这串字符串？例如，你想要的字符串是 "What's your name?"。你不能指定 'What's your name?'，因为这会使 Python 对于何处是字符串的开始、何处又是结束而感到困惑
你必须指定这个单引号不代表这串字符串的结尾。这可以通过 转义序列（Escape Sequence） 来实现。你通过 \ 来指定单引号：要注意它可是反斜杠。现在，你可以将字符串指定为 'What\'s your name?'

使用一个表示新一行的转义序列——\n 来表示新一行的开始
`'This is the first line\nThis is the second line'`

一个放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行

```python
"This is the first sentence. \
This is the second sentence." #"This is the first sentence. This is the second sentence."
```

如果你需要指定一些未经过特殊处理的字符串，比如转义序列，那么你需要在字符串前增加 r 或 R 来指定一个 原始（Raw） 字符串

`r"Newlines are indicated by \n"`

## 字符串方法

我们可以通过使用字符串方法来对字符串进行操作。

.strip(): 去除首尾空白字符

.split(): 分割字符串（默认为空格）

.replace(): 替换字符

.find(): 查找字符

.count(): 字符计数

.upper()/.lower(): 转大/小写

.ljust()/rjust()/zfill(): 指定宽度

.isalpha()/isdigit()/.isalnum()

```python
#join & split
>>>"+".join(['a','b','c'])
a+b+c
>>>"a+b+c".split("+")
['a','b','c']
>>>"I'm fine".split()
["I'm","fine"]
>>>"I'm fine".split("'")
["I","m fine"]
```

```python
#replace & find
a="abcdacd"
a.replace('a' ,'b')
a.replace('a' ,'b').replace('b' ,'c')
a.find ('a')
a.rfind('a')
a.count('a')
```

```python
#isalnum 
#Python isalnum() 方法检测字符串是否由字母和数字组成
#string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
a='hello'
help(a.isalnum)
print(a.isalnum())          #True
print("1234".isalnum())     #True
print("123abc".isalnum())   #True
print("1.23".isalnum())     #False
print("123.abc".isalnum())  #False
```

## 数据类型

布尔类型：True/False

数字：1234，3.14159，3+4j

字符串：'hello', "I'm", """a\nb ""

列表(list)：[1,[2,'three'],4]

字典(dict)：{'name':"zhang","age":18}

元组(Tuple):(1,'spam',4,'K')

集合(set):set('abca'),{'a','b','c'}

## 布尔类型

```python
>>> bool('')
False
>>> bool('hello')True
>>> a = None
>>> b = 1
>>> bool(a)
False
>>> bool(b)True
```

```python
>>> not 1==3        
True
>>> 1>2 or 2>1      
True
>>> (1>2) + (2>1)  
1                   
>>> (1>2) and (2>1)  
False
>>> (1>2) * (2>1)    
0
```

## 逻辑行与物理行

如果你希望在一行物理行中指定多行逻辑行，那么你必须通过使用分号(;)来明确表明逻辑行或语句的结束

```python
i = 5       #i = 5;
print(i)    #i = 5;
```

## 核心：运算符与表达式

```python
+（加）两个对象相加。3+5 则输出 8。'a' + 'b' 则输出 'ab'。
-（减）从一个数中减去另一个数，如果第一个操作数不存在，则假定为零。-5.2 将输出一个负数，50 - 24 输出 26。
*（乘）给出两个数的乘积，或返回字符串重复指定次数后的结果。2 * 3 输出 6。'la' * 3 输出 'lalala'。
** （乘方）返回 x 的 y 次方。3 ** 4 输出 81 （即 3 * 3 * 3 * 3）。
/ （除）x 除以 y13 / 3 输出 4.333333333333333。
// （整除）x 除以 y 并对结果向下取整至最接近的整数。13 // 3 输出 4。-13 // 3 输出 -5。
% （取模）返回除法运算后的余数。13 % 3 输出 1。-25.5 % 2.25 输出 1.5。
<< （左移）将数字的位向左移动指定的位数。（每个数字在内存中以二进制数表示，即 0 和1）2 << 2 输出 8。 2 用二进制数表示为 10。向左移 2 位会得到 1000 这一结果，表示十进制中的 8。
>> （右移）将数字的位向右移动指定的位数。11 >> 1 输出 5。11 在二进制中表示为 1011，右移一位后输出 101 这一结果，表示十进制中的 5。
& （按位与）对数字进行按位与操作。5 & 3 输出 1。
| （按位或）对数字进行按位或操作。5 | 3 输出 7。
^（按位异或）对数字进行按位异或操作。5 ^ 3 输出 6。
~ （按位取反）x 的按位取反结果为 -(x+1)。~5 输出 -6。有关本例的更多细节可以参阅：http://stackoverflow.com/a/11810203 。
< （小于）返回 x 是否小于 y。所有的比较运算符返回的结果均为 True 或 False。请注意这些名称之中的大写字母。5 < 3 输出 False，3 < 6 输出 True。比较可以任意组成组成链接：3 < 5 < 7 返回 True。
> （大于）返回 x 是否大于 y。5 > 3 返回 True。如果两个操作数均为数字，它们首先将会被转换至一种共同的类型。否则，它将总是返回 False。
<= （小于等于）返回 x 是否小于或等于 y。x = 3; y = 6; x<=y 返回 True。
>= （大于等于）返回 x 是否大于或等于 y。x = 4; y = 3; x>=3 返回 True。
== （等于）比较两个对象是否相等。x = 2; y = 2; x == y 返回 True。x = 'str'; y = 'stR'; x == y 返回 False。x = 'str'; y = 'str'; x == y 返回 True。
!= （不等于）比较两个对象是否不相等。x = 2; y = 3; x != y 返回 True。
not （布尔“非”）如果 x 是 True，则返回 False。如果 x 是 False，则返回 True。x = True; not x 返回 False。
and （布尔“与”）如果 x 是 False，则 x and y 返回 False，否则返回 y 的计算值。当 x 是 False 时，x = False; y = True; x and y 将返回 False。在这一情境中，Python 将不会计算 y，因为它已经了解 and 表达式的左侧是 False，这意味着整个表达式都将是 False 而不会是别的值。这种情况被称作短路计算（Short-circuit Evaluation）。
or（布尔“或”）如果 x 是 True，则返回 True，否则它将返回 y 的计算值。x = Ture; y = False; x or y 将返回 Ture。在这里短路计算同样适用
```

## 数值运算与赋值的快捷方式

```python
#变量 = 变量 运算 表达式 会演变成 变量 运算 = 表达式
a = 2       #a = 2
a = a * 3   #a *= 3
```

## 求值顺序

```python
lambda：Lambda 表达式
if - else ：条件表达式
or：布尔“或”
and：布尔“与”
not x：布尔“非”
in, not in, is, is not, <, <=, >, >=, !=, ==：比较，包括成员资格测试（Membership Tests）和身份测试（Identity Tests）。
|：按位或
^：按位异或
&：按位与
<<, >>：移动
+, -：加与减
*, /, //, %：乘、除、整除、取余
+x, -x, ~x：正、负、按位取反
**：求幂
x[index], x[index:index], x(arguments...), x.attribute：下标、切片、调用、属性引用
(expressions...), [expressions...], {key: value...}, {expressions...}：表示绑定或元组、表示列表、表示字典、表示集合
```

## 改变运算顺序

`2 + (3 * 4) 自是要比 2 + 3 * 4` 要更加容易理解，因为后者还要求你要了解运算符的优先级

`(2 + 3) * 4` :使用括号还有一个额外的优点——它能帮助我们改变运算的顺序。同样举个例子，如果你希望在表达式中计算乘法之前应先计算加法，那么你可以将表达式写作

## 核心：控制流

```python
#猜数字
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    # 新块从这里开始
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # 新块在这里结束
elif guess < number:
    # 另一代码块
    print('No, it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
else:
    print('No, it is a little lower than that')
    # 你必须通过猜测一个大于（>）设置数的数字来到达这里。
print('Done')
# 这最后一句语句将在
# if 语句执行完毕后执行。
```

## while 语句

```python
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事
print('Done')
```

## for 循环

```python
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
```

我们通过内置的 range 函数生成这一数字序列。
在这里我们所要做的事情是提供两个数字，而 range 将会返回一个数字序列，从第一个数字开始，至第二个数字结束。举个例子，range(1,5) 将输出序列 [1, 2, 3, 4]。在默认情况下，range 将会以 1 逐步递增。如果我们向 range 提供第三个数字，则这个数字将成为逐步递增的加数。同样举个例子来说明，range(1,5,2) 将会输出 [1, 3]。要记住这一序列扩展直到第二个数字，也就是说，它不会包括第二个数字在内.

```python
>>>range(10)        # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)     # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)  # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)  # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
>>> range(1,30,5) #1 6 11 16 21 26
```

另外需要注意的是，range() 每次只会生成一个数字，如果你希望获得完整的数字列表，要在使用 range() 时调用 list()。例如下面这样：list(range(5)) ，它将会返回 [0, 1, 2, 3, 4]

## break 语句

```python
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
```

## continue 语句

```python
#continue 语句用以告诉 Python 跳过当前循环块中的剩余语句，并继续该循环的下一次迭代
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理
```

## 核心：数据结构
