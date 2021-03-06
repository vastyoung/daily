# python

```python
# https://docs.python.org/zh-cn/3/tutorial/inputoutput.html
# f 后面可接 {} 表达式
ss_log.info(f"please choose a config from 1-{len(configs)}")
```

```python
# 单星号（*）：*agrs :将所有参数以元组的形式导入
def foo(param1, *param2):
    print (param1)      # 1
    print (param2)      # (2，3，4，5)
foo(1,2,3,4,5)

# 双星号（**）：**kwargs :将所有参数以字典的形式导入
def bar(param1, **param2):
    print (param1)       # 1
    print (param2)       # {'a':2，'b': 3}
bar(1,a=2,b=3)
```

在你的操作系统中开启终端程序然后通过输入python并按下回车键来打开 Python 提示符

`print("Hello World")` :打印 Hello World

退出解释器环境可以通过按下 [ctrl + d] 组合键或是输入 exit() （注意：要记住要包含括号 ()）并敲下回车实现

`python hello.py` :运行 hello.py 程序

`help('len')` :显示出有关 len 函数的帮助

## 创建独立的 python 虚拟环境

```bash
python3 -m venv ~/Pyvenv/venv3/
```

## 基础：基本概念

### 注释

`print('hello world')` #注意 print 是一个函数

```python
# 注意 print 是一个函数
print('hello world')

```

### 变量

命名需要遵守以下规则：

第一个字符必须是字母表中的字母（大写 ASCII 字符或小写 ASCII 字符或 Unicode 字符）或下划线（_）。

其它部分可以由字符（大写 ASCII 字符或小写 ASCII 字符或 Unicode 字符）、下划线（_）、数字（0~9）组成。

名称区分大小写。例如，myname 和 myName 并不等同。要注意到前者是小写字母 n 而后者是大写字母 N。

有效的名称可以是 i 或 name_2_3 ，而 2things，this is spaced out，my-name 或 >a1b2_c3都是无效 的名称。

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

### 转义序列

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

### 字符串方法

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

### 数据类型

布尔类型：True/False

数字：1234，3.14159，3+4j

字符串：'hello', "I'm", """a\nb ""

列表(list)：[1,[2,'three'],4]

字典(dict)：{'name':"zhang","age":18}

元组(Tuple):(1,'spam',4,'K')

集合(set):set('abca'),{'a','b','c'}

### 布尔类型

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

### 逻辑行与物理行

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

### 数值运算与赋值的快捷方式

```python
#变量 = 变量 运算 表达式 会演变成 变量 运算 = 表达式
a = 2       #a = 2
a = a * 3   #a *= 3
```

### 求值顺序

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

### 改变运算顺序

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

### while 语句

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

### for 循环

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

### break 语句

```python
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')
```

### continue 语句

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

```python
a = [99 , "bottles of beer", ["on", "the", "wall"]]

>>>a[0] = 9
>>>a[1:2] = ["bottles", "of", "beer"]
>>>print(a)
[98, "bottles", "of", "beer", ["on", "the", "wall"]]
>>>del a[-1]
>>>print(a)
[98, "bottles", "of", "beer"]
```

```python
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')# I have 4 items to purchase.

print('These items are:', end=' ')          # 为末尾end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符
for item in shoplist:
    print(item, end=' ')                    # These items are: apple mango carrot banana

print('\nI also have to buy rice.')         # \n 换行符

shoplist.append('rice')
print('My shopping list is now', shoplist)  # My shopping list is now ['apple', 'mango', 'carrot', 'banana', 'rice']
print('I will sort my list now')            # I will sort my list now

shoplist.sort() # 排序
print('Sorted shopping list is', shoplist)          # Sorted shopping list is ['apple', 'banana', 'carrot', 'mango', 'rice']
print('The first item I will buy is', shoplist[0])  # The first item I will buy is apple

olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)              # I bought the apple
print('My shopping list is now', shoplist)  # My shopping list is now ['banana', 'carrot', 'mango', 'rice']
```

### 列表方法

```python
>>> a = range(5)      # [0,1,2,3,4]
>>> print(list(a))
>>> a.append(5)       # [0,1,2,3,4,5]
#最先进入的元素最后一个被释放（后进先出）。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来
>>> a.pop()           # [0,1,2,3,4]
5
>>> a.insert(0, 42)   # [42,0,1,2,3,4]
>>> a.pop(0)          # [0,1,2,3,4]
42
#sort() 函数用于对原列表进行排
>>> a.sort()          # [0,1,2,3,4]
>>> a.reverse()       # [4,3,2,1,0]
# 字符串排序使用字典序,逐位比较字母
```

### 列表函数

```python
# range()  生成数组列表
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2, 30, 5))
[2, 7, 12, 17, 22, 27] 
# sum()   求和
# min()   返回列表中最小元素
# max()   返回列表中最大元素
```

### 列表排序

```python
mylist = ["b", "C", "A", "a"]
# method of list
mylist.sort()
mylist.sort(key=str.lower)
# general function
nlist = sorted(mylist)
nlist = sorted(mylist,reverse=True)
```

### 元组

元组（Tuple）用于将多个对象保存到一起。你可以将它们近似地看作列表，但是元组不能提供列表类能够提供给你的广泛的功能。元组的一大特征类似于字符串，它们是不可变的，也就是说，你不能编辑或更改元组.

```python
# 我会推荐你总是使用括号
# 来指明元组的开始与结束
# 尽管括号是一个可选选项。
# 明了胜过晦涩，显式优于隐式。
zoo = ('python', 'elephant', 'penguin')

print('Number of animals in the zoo is', len(zoo))          # Number of animals in the zoo is 3

new_zoo = 'monkey', 'camel', zoo

print('Number of cages in the new zoo is', len(new_zoo))    # Number of cages in the new zoo is 3

print('All animals in new zoo are', new_zoo)                # All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))

print('Animals brought from old zoo are', new_zoo[2])       # Animals brought from old zoo are ('python', 'elephant', 'penguin')

print('Last animal brought from old zoo is', new_zoo[2][2]) # Last animal brought from old zoo is penguin

print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))                       # Number of animals in the new zoo is 5
```

### 字典

字典就像一本地址簿，如果你知道了他或她的姓名，你就可以在这里找到其地址或是能够联系上对方的更多详细信息，换言之，我们将键值（Keys）（即姓名）与值（Values）（即地址等详细信息）联立到一起。在这里要注意到键值必须是唯一的，正如在现实中面对两个完全同名的人你没办法找出有关他们的正确信息。

```python
# “ab”是地址（Address）簿（Book）的缩写
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])    # Swaroop's address is swaroop@swaroopch.com

# 删除一对键值—值配对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))  # There are 3 contacts in the address-book

#items() 方法的遍历：items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回。
for name, address in ab.items():                        # Contact Swaroop at swaroop@swaroopch.com
    print('Contact {} at {}'.format(name, address))     # Contact Matsumoto at matz@ruby-lang.org
                                                        # Contact Larry at larry@wall.org                           
                                                        
# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])      # Guido's address is guido@python.org
```

### 字典构造

```python
sub = {'zhao':1, 'li':2, 'qian':3}
print(sub)
sub = dict(zhao = 1, li = 2, qian = 3)
print(sub)
keys = ['zhao', 'li', 'qian', 'sun']
vals = [1, 2 ,3, 4]
sub = dict(zip(keys,vals))
print(sub)
```

### 字典方法

```python
# Keys, values, items:
d.keys()  -> ["duck", "back"]
d.values()  -> ["duik", "rug"]
d.items() -> [("duck","duik"), ("back","rug")]
# 存在性检验
d.has_key("duck") -> 1; d.has_key("spam") -> 0
# 键值类型均随意
{"name":"Guido", "age":43, ("hello","world"):1, 42:"yes", "flag":["red", "white", "blue"]}
```

### 字典遍历

```python
d = dict(a=12, b="abc",c=15)
print(d)
for item in d.items():
    print(item)
for key in d:
    print(key,d[key])
for value in d.values():
    print(value)
```

### 字典排序

```python
disordered = {10: 'b', 3: 'a', 5: 'c'}
sorted_dict = {k: disordered[k] for k in sorted(disordered)}
print(sorted_dict)
sorted_dict = sorted([(v,k) for (k,v) in disordered.items()], reverse=True)
print(sorted_dict)
```

### 序列

```python
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
# Indexing or 'Subscription' operation #
# 索引或“下标（Subscription）”操作符 #
print('Item 0 is', shoplist[0])             # Item 0 is apple

print('Item 1 is', shoplist[1])             # Item 1 is mango

print('Item 2 is', shoplist[2])             # Item 2 is carrot

print('Item 3 is', shoplist[3])             # Item 3 is banana

print('Item -1 is', shoplist[-1])           # Item -1 is banana

print('Item -2 is', shoplist[-2])           # Item -2 is carrot

print('Character 0 is', name[0])            # Character 0 is s

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])      # Item 1 to 3 is ['mango', 'carrot']

print('Item 2 to end is', shoplist[2:])     # Item 2 to end is ['carrot', 'banana']

print('Item 1 to -1 is', shoplist[1:-1])    # Item 1 to -1 is ['mango', 'carrot']

print('Item start to end is', shoplist[:])  # Item start to end is ['apple', 'mango', 'carrot', 'banana']

# 从某一字符串中切片 #
print('characters 1 to 3 is', name[1:3])    # characters 1 to 3 is wa

print('characters 2 to end is', name[2:])   # characters 2 to end is aroop

print('characters 1 to -1 is', name[1:-1])  # characters 1 to -1 is waroo

print('characters start to end is', name[:])# characters start to end is swaroop
```

你同样可以在切片操作中提供第三个参数，这一参数将被视为切片的步长（Step）（在默认情况下，步长大小为 1）：

```python
>>> shoplist = ['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::1]
['apple', 'mango', 'carrot', 'banana']
>>> shoplist[::2]
['apple', 'carrot']
>>> shoplist[::3]
['apple', 'banana']
>>> shoplist[::-1]
['banana', 'carrot', 'mango', 'apple']
```

你会注意到当步长为 2 时，我们得到的是第 0、2、4…… 位项目。当步长为 3 时，我们得到的是第 0、3……位项目。

### 集合

```python
>>> bri = set(['brazil', 'russia', 'india'])
>>> 'india' in bri
True

>>> 'usa' in bri
False

>>> bric = bri.copy()
>>> bric.add('china')
#issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False
>>> bric.issuperset(bri)
True
>>> bri.remove('russia')
>>> bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
```

### 引用

```python
print('Simple Assignment')                          # Simple Assignment
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist
# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0]
print('shoplist is', shoplist)                      # shoplist is ['mango', 'carrot', 'banana']
print('mylist is', mylist)                          # mylist is ['mango', 'carrot', 'banana']
# 注意到 shoplist 和 mylist 二者都
# 打印出了其中都没有 apple 的同样的列表，以此我们确认
# 它们指向的是同一个对象
print('Copy by making a full slice')                # Copy by making a full slice
# 通过生成一份完整的切片制作一份列表的副本
mylist = shoplist[:]
# 删除第一个项目
del mylist[0]
print('shoplist is', shoplist)                      # shoplist is ['mango', 'carrot', 'banana']
print('mylist is', mylist)                          # mylist is ['carrot', 'banana']
# 注意到现在两份列表已出现不同

```

```python
# 这是一个字符串对象
name = 'Swaroop'
if name.startswith('Swa'):                          # startswith() 方法用于检查字符串是否是以指定子字符串开头
    print('Yes, the string starts with "Swa"')      # Yes, the string starts with "Swa"
if 'a' in name:
    print('Yes, it contains the string "a"')        # Yes, it contains the string "a"
if name.find('war') != -1:                          #  find() 方法检测字符串中是否包含子字符串 str 
    print('Yes, it contains the string "war"')      # Yes, it contains the string "war"
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']     # Brazil_*_Russia_*_India_*_China
print(delimiter.join(mylist))                       # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
```

## 核心：函数

函数（Functions）是指可重复使用的程序片段。它们允许你为某个代码块赋予名字，允许你通过这一特殊的名字在你的程序任何地方来运行代码块，并可重复任何次数。这就是所谓的调用（Calling）函数。我们已经使用过了许多内置的函数，例如 len 和 range

```python
def say_hello():
    # 该块属于这一函数
    print('hello world')
# 函数结束
say_hello()  # 调用函数     # hello world
say_hello()  # 再次调用函数 # hello world
```

```python
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
# 直接传递字面值
print_max(3, 4)     # 4 is maximum
x = 5
y = 7
# 以参数的形式传递变量
print_max(x, y)     # 7 is maximum
```

第一次调用函数 print_max 时，我们以实参的形式直接向函数提供这一数字。在第二次调用时，我们将变量作为实参来调用函数。print_max(x, y) 将使得实参 x 的值将被赋值给形参 a，而实参 y 的值将被赋值给形参 b。在两次调用中，print_max 都以相同的方式工作。

### 局部变量

```python
x = 50
def func(x):
    print('x is', x)                    # x is 50
    x = 2
    print('Changed local x to', x)      # Changed local x to 2
func(x)
print('x is still', x)                  # x is still 50
```

### global 语句

如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的。我们需要通过 global 语句来完成这件事。因为在不使用 global 语句的情况下，不可能为一个定义于函数之外的变量赋值。

```python
x = 50
def func():
    global x
        print('x is', x)                # x is 50
    x = 2
    print('Changed global x to', x)     # Changed global x to 2

func()

print('Value of x is', x)               # Value of x is 2
```

global 语句用以声明 x 是一个全局变量——因此，当我们在函数中为 x 进行赋值时，这一改动将影响到我们在主代码块中使用的 x 的值。

### 默认参数值

```python
def say(message, times=1):
    print(message * times)

say('Hello')        # Hello
say('World', 5)     # WorldWorldWorldWorldWorld
```

### 关键字参数

```python
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)              # a is 3 and b is 7 and c is 10
func(25, c=24)          # a is 25 and b is 5 and c is 24
func(c=50, a=100)       # a is 100 and b is 5 and c is 50
```

### 可变参数

```python
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

#输出:
$ python function_varargs.py
a 10
single_item 1
single_item 2
single_item 3
Inge 1560
John 2231
Jack 1123
None
```

### return 语句

```python
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
print(maximum(2, 3))

#输出:
$ python function_return.py
3
```

### DocStrings

```python
def print_max(x, y):
    '''打印两个数值中的最大数。
    这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)

#输出:

$ python function_docstring.py
5 is maximum
打印两个数值中的最大数。
    这两个数都应该是整数
```

## 核心：模块

```python
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

#输出:

$ python module_using_sys.py we are arguments
The command line arguments are:
module_using_sys.py
we
are
arguments
The PYTHONPATH is ['/tmp/py',
# many entries here, not shown here
'/Library/Python/2.7/site-packages',
'/usr/local/lib/python2.7/site-packages']
```

### from..import 语句

如果你希望直接将 argv 变量导入你的程序（为了避免每次都要输入 sys.），那么你可以通过使用 from sys import argv 语句来实现这一点。
警告：一般来说，你应该尽量避免使用 from...import 语句，而去使用 import 语句。这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。

```python
from math import sqrt
print("Square root of 16 is", sqrt(16))
```

### 模块的 __name__

```python
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

#输出:
$ python module_using_name.py
This program is being run by itself
$ python
>>> import module_using_name
I am being imported from another module
>>>
```

```python
def say_hi():
    print('Hi, this is mymodule speaking.')
__version__ = '0.1'

```

```python
import mymodule
mymodule.say_hi()
print('Version', mymodule.__version__)

#输出:
$ python mymodule_demo.py
Hi, this is mymodule speaking.
Version 0.1
```

```python
from mymodule import say_hi, __version__
say_hi()
print('Version', __version__)
```

`from mymodule import *` :这将导入诸如 say_hi 等所有公共名称，但不会导入 __version__ 名称，因为后者以双下划线开头。

### dir 函数

```python
$ python
>>> import sys
# 给出 sys 模块中的属性名称
>>> dir(sys)
['__displayhook__', '__doc__',
'argv', 'builtin_module_names',
'version', 'version_info']
# 此处只展示部分条目
# 给出当前模块的属性名称
>>> dir()
['__builtins__', '__doc__',
'__name__', '__package__','sys']
# 创建一个新的变量 'a'
>>> a = 5
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'a']
# 删除或移除一个名称
>>> del a
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
```

## 核心：输入输出

```python
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")

#输出:
$ python3 io_input.py
Enter text: sir
No, it is not a palindrome
$ python3 io_input.py
Enter text: madam
Yes, it is a palindrome
$ python3 io_input.py
Enter text: racecar
Yes, it is a palindrome
```

我们同样可以提供第三个参数来确定切片的步长（Step）。默认的步长为 1，它会返回一份连续的文本。如果给定一个负数步长，如 -1，将返回翻转过的文本
input() 函数可以接受一个字符串作为参数，并将其展示给用户。尔后它将等待用户输入内容或敲击返回键。一旦用户输入了某些内容并敲下返回键，input() 函数将返回用户输入的文本。
我们获得文本并将其进行翻转。如果原文本与翻转后的文本相同，则判断这一文本是回文。

### 文件

```python
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''
# 打开文件以编辑（'w'riting）
f = open('poem.txt', 'w')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()
# 如果没有特别指定，
# 将假定启用默认的阅读（'r'ead）模式
f = open('poem.txt')
while True:
    line = f.readline()
    # 零长度指示 EOF
    if len(line) == 0:
        break
    # 每行（`line`）的末尾
    # 都已经有了换行符
    #因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()

#输出:
$ python3 io_using_file.py
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
```

首先，我们使用内置的 open 函数并指定文件名以及我们所希望使用的打开模式来打开一个文件。打开模式可以是阅读模式（'r'），写入模式（'w'）和追加模式（'a'）。我们还可以选择是通过文本模式（'t'）还是二进制模式（'b'）来读取、写入或追加文本。实际上还有其它更多的模式可用，help(open) 会给你有关它们的更多细节。在默认情况下，open() 会将文件视作文本（text）文件，并以阅读（read）模式打开它。

### Pickle

```python
import pickle
# 我们存储相关对象的文件的名称
shoplistfile = 'shoplist.data'
# 需要购买的物品清单
shoplist = ['apple', 'mango', 'carrot']
# 准备写入文件
f = open(shoplistfile, 'wb')
# 转储对象至文件
pickle.dump(shoplist, f)
f.close()
# 清除 shoplist 变量
del shoplist
# 重新打开存储文件
f = open(shoplistfile, 'rb')
# 从文件中载入对象
storedlist = pickle.load(f)
print(storedlist)

#输出:
$ python io_pickle.py
['apple', 'mango', 'carrot']
```

要想将一个对象存储到一个文件中，我们首先需要通过 open 以写入（write）二进制（binary）模式打开文件，然后调用 pickle 模块的 dump 函数。这一过程被称作封装（Pickling）。
接着，我们通过 pickle 模块的 load 函数接收返回的对象。这个过程被称作拆封（Unpickling）

### Unicode

```python
>>> "hello world"
'hello world'
>>> type("hello world")
<class 'str'>
>>> u"hello world"
'hello world'
>>> type(u"hello world")
<class 'str'>
```

```python
# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)
```

## 核心：标准库

系统内置模块

```python
os ： 对操作系统服务提供了可移植的（ portable）的接口。
sys： 包括跟python解析器和环境相关的变量和函数。
decimal： python中的float使用双精度的二进制浮点编码来表示的，这种编码导致了小数不能被精确的表示，例如0.1实际上内存中为0.100000000000000001，还有3*0.1 == 0.3 为False.decimal就是为了解决类似的问题的，拥有更高的精确度，能表示更大范围的数字，更精确地四舍五入。
math： 定义了标准的数学方法，例如cos(x),sin(x)等。
random： 随机数生成。
string： 包含大量处理字符串的函数。
io： 实现了各种IO形式和内置的open()函数。
datetime： 时间日期相关函数。
timeit： 计时函数，调试相关。
logging： 将一些调试（Debugging）信息或一些重要的信息储存在某个地方。
```

### OS 模块

```python
os.name： 获取当前体系平台， Windows下返回""nt""， Linux下返回""posix""。
os.linesep： 获取当前平台应用的行终止符。 Windows下返回""/r/n""， Linux应用""/n""。
os.getcwd(): 获取当前工作目录，即当前python脚本工作的目录路径。
os.listdir(path)：返回指定目录下的所有文件和目录名。
os.path.split()：分离路径中的目录名和文件名。
os.path.exists()：检查路径是否存在。
os.path.isfile()： 判断是否为文件。
```

```python
>>> import os
>>> print(os.getcwd())
>>> print(os.listdir("D:\\"))
>>> print(os.path.exists("D:\\test"))
```

### sys 模块

```python
>>> import sys
>>> sys.version_info
sys.version_info(major=3, minor=5, micro=1, releaselevel='final', serial=0)
>>> sys.version_info.major == 3
True
```

sys 模块包含一个 version_info 元组，它提供给我们版本信息。第一个条目是主版本信息。我们可以调出这些信息并使用它。
除此之外，sys 模块还有以下功能：
sys.argv 获取命令行传入参数。– sys.argv[0] 为脚本名， sys.argv[1] 为第一个参数sys.getdefaultencoding(): 获取当前终端编码，一般默认为ascii。sys.getfilesystemencoding(): 获取文件系统编码， Windows下返回""mbcs""， mac下返回""utf-8""。sys.path: 命令搜索路径。

### decimal 模块

```python
>>> a="%.20f" %(1/3.)
>>> a="%.20f" %(2.645)
>>> a="%.20f" %(2.675)
>>> round(2.675,2)
>>> print(0.1+0.1+0.1-0.3)
5.55111512313e-17
>>> from decimal import Decimal as D
>>> D('0.1') + D('0.1') + D('0.1') - D('0.3')
Decimal("0.0")
```

### decimal 精度控制

```python
>>> from decimal import Decimal as D
>>> from decimal import getcontext
>>> getcontext().prec
28
>>> D(1)/D(7)
Decimal('0.1428571428571428571428571429')
>>> getcontext().prec=6
>>> D(1)/D(7)
Decimal('0.142857')
>>> D(str(1.12)/D(7))
```

### math 数学模块

```python
>>> import math
>>> math.pi
>>> math.e
>>> math.sin(2*math.pi/180)
>>> math.fmod(9.8,4.0)
```

### random 模块

```python
>>> import random
>>> random.randint(0,99) #随机整数
>>> random.randrange(0, 101, 2) #随机偶数
>>> random.random() #随机浮点数
>>> random.uniform(1, 10) #均匀分布
>>> random.choice('?abc&%^*f') #随机字符
>>> random.sample('abcdefghij',3)
>>> items = [1, 2, 3, 4, 5, 6]
>>> random.shuffle(items) #洗牌
```

### datetime 模块

```python
>>> import datetime as dt
>>> print('date.max:', dt.date.max)
>>> print('date.min:', dt.date.min)
>>> print('date.today():', dt.date.today())
>>> dt.date.isoweekday(dt.date.today())
>>> dt.date.today()+dt.timedelta(7)
>>> print('Time:', dt.time(12,5,4))
>>> dt.datetime.now()
```

### 时间与字符串

```python
>>> from datetime import datetime as dtdt
>>> dtdt.now()
>>> dtdt.strftime(dtdt.now(),'%c')
>>> d = dtdt.now() - dtdt.strptime('2015/12/2020:56:30','%Y/%m/%d %H:%M:%S')
>>> (d.days, d.seconds, d.microseconds)
```

### timeit 模块

```python
>>> import timeit as ti
>>> t = ti.Timer('x=range(100)')
>>> t.timeit()
>>> t.timeit(100)
>>> ti.timeit('x=range(100)',number=100)
>>> t.repeat(3, 20000)
```

### 日志模块

```python
import os
import platform
import logging
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')
print("Logging to", logging_file)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

#输出:
$ python stdlib_logging.py
Logging to /Users/swa/test.log
$ cat /Users/swa/test.log
2014-03-29 09:27:36,660 : DEBUG : Start of the program
2014-03-29 09:27:36,660 : INFO : Doing something
2014-03-29 09:27:36,660 : WARNING : Dying now
```

## 科学计算 numpy和scipy

```python
Numpy：Arrays manipulation library 科学计算的必装模块，几乎所有的其他科学模块都依赖于它
Scipy：扩展的科学计算模块
PyGSL：C/C++语言中著名的科学计算函数库GNU Scientific Library(GSL)的python版
Matplotlib：高质量的2D作图模块，足以替代GNUPlot
Mayavi：强大的三维作图模块，属于EPD公司套件的一部分（注意：此模块支持Python2，官方未支持Python3）
Sympy：符号计算模块
StatLib：统计学工具箱
Escript/Finley：偏微分方程求解
Parallel Python：并行计算模块
```

### Numpy数组创建

```python
>>> import numpy as np
>>> a = np.array([1, 2, 3, 4], dtype='int32')
>>> a = np.array([[3,4,5],[3,6,7]])
np.arange(0,1,0.1) np.zeros(2,3) np.ones(5)
np.linspace(0, 1, 12) np.logspace(0, 2, 20)
```

函数式创建：

```python
def func(i, j):
    return (i+1) * (j+1)
a = np.fromfunction(func, (9,9))
```

### np.array 与 list 的区别

```python
>>> a=range(5)
>>> a + 1
>>> a * 2
>>> a + a
>>> a > 3
>>> np.array(a)
>>> b=np.arange(5)
>>> b + 1
>>> b * 2
>>> b + b
>>> b > 3
>>> b / 2
>>> list(b)
```

### 一维数组取样

```python
>>> a = np.arange(10)
>>> a[5] # 用整数作为下标可以获取数组中的某个元素
>>> a[3:5] # 用范围作为下标获取数组的一个切片，包括a[3]不包括a[5]
>>> a[:5] # 省略开始下标，表示从a[0]开始
>>> a[:-1] # 下标可以使用负数，表示从数组后往前数，array([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> a[2:4] = 100,101 # 下标还可以用来修改元素的值
>>> a[1:-1:2] # 范围中的第三个参数表示步长， 2表示隔一个元素取一个元素
```

### 二维数组取样

```python
>>> a = np.arange(10).reshape(2,-1)
>>> a
array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9]])
>>> a[1,1] #单个元素
6
>>> a[1] #整行
array([5, 6, 7, 8, 9])
>>> a[:,2] #整列
array([2, 7])
>>> a[0][::2] #抽取某行特定元素
array([0, 2, 4])
```

### 条件取样

```python
>>> a = np.arange(10).reshape(-1,2)
>>> a[a[:,1]>3]
array([[4, 5],
       [6, 7],
       [8, 9]])
>>> a[a[:,1]%3==0]
array([[2, 3],
       [8, 9]])
>>> a[(a[:,1]>3)*(a[:,1]%3==0)]
```

### 数组排序

```python
#argsort函数返回数组值从小到大的索引
>>> x = np.array([3,1,2])
>>> np.argsort(x)
>>> x[np.argsort(x)] # 排序后的数组
>>> x=np.array([[0,3],[4,2]])
>>> np.argsort(x, axis=1) # 排序每行
>>> a[a[:,1].argsort()] # 按第二列排序
```

### 数学数组方法

```python
>>> a = np.arange(6).reshape(2,3)
>>> a.shape 
(2, 3)
>>> a.dtype 
dtype('int32')
分别试试a.sum() a.min() a.max() a.mean()
>> a.reshape(3,2) #转置a.T
>> a.ravel() #展开数组
>> a.repeat(2,axis=0) #复制元素
```

### 数组合并

```python
>>> a = np.array([1, 2, 3])
>>> b = np.array([2, 3, 4])
>>> np.r_[a,b]
>>> np.hstack((a,b))
array([1, 2, 3, 2, 3, 4])
>>> np.vstack((a,b))
array([[1, 2, 3],
       [2, 3, 4]])
>>> np.c_[a,b]
array([[1, 2],
       [2, 3],
       [3, 4]])
```

### 数据存储

```python
numpy.savetxt(fname, X, fmt='%.18e',delimiter=' ', newline='\n', header='',footer='', comments='# ')
>>> x = y = z = np.arange(0.0,5.0,0.5)
>>> np.savetxt('test.out', x, delimiter=',')
# X is an array
>>> np.savetxt('test.out', (x,y,z))
# x,y,z equal sized 1D arrays
>>> np.savetxt('test.out', x, fmt='%6.4f')you
# use exponential notation
```

### 数据读取

```python
numpy.loadtxt(fname, dtype=<type 'float'>,comments='#', delimiter=None,converters=None, skiprows=0, usecols=None,unpack=False, ndmin=0)
让我们来读取刚才已经存储的数据
>>> data = np.loadtxt('test.out', dtype = float)
>>> data = np.loadtxt('test.out', usecols=[1])
```

### 和math函数比较

```python
import time, math
import numpy as np
n = 1e+6
x = range(int(n))
start = time.clock()
for i in x:
    tmp = math.sin(i/n)
print("math.sin:", time.clock() - start)
x = np.array(x)/n
start = time.clock()
np.sin(x)
print("numpy.sin:", time.clock() - start)
```

## 绘图模块 matplotlib

```python

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x) ; z = np.cos(x**2)
plt.figure()
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.legend(loc=3)
plt.show() #保存图像可用 plt.savefig('fig.jpg')
plt.close()
```

### Plot参数

```python
• alpha : float
• color or c : any matplotlib color
• label : any string , 图注名称
• linestyle or ls : [ '-' | '--' | '-.' | ':' | 'steps' | ...]
• linewidth or lw: float value (points, 0.3527mm )
• marker [ '+' | ',' | '.' | '1' | '2' | '3' | '4' ]
• markersize or ms : float
• zorder: any number 叠放顺序
```

### 颜色

```python
• 蓝色： 'b' (blue)
• 绿色： 'g' (green)
• 红色： 'r' (red)
• 青色： 'c' (cyan)
• 洋红： 'm' (magenta)
• 黄色： 'y' (yellow)
• 黑色： 'k' (black)
• 白色： 'w' (white)
• 灰度表示： e.g. 0.75 ([0,1]内任意浮点数)
• RGB表示法： 由红色、绿色和蓝色的值组成的十六进制符号来定义 e.g. '#2F4F4F' 或 (0.18,0.31,0.31)
```

### 坐标轴定制

```python
• plt.title('sine function demo')
• plt.xlabel('time(s)')
• plt.ylabel('votage(mV)')
• plt.xlim([0.0,5.0])
• plt.ylim([-1.2,1.2])
• plt.hold('on') # 保持之前plot的结果
• plt.grid('on') # 添加网格
• plt.text(4,0,'$\mu=100$') # 文本
• plt.axis('equal') # 等比例坐标轴
• plt.ylim(plt.ylim()[::-1]) # 翻转Y轴
• plt.gca().invert_yaxis() # 翻转Y轴
```

### 极坐标

```python
import numpy as np
import matplotlib.pyplot as plt
r = np.arange(0, 3.0, 0.01)
theta = 2 * np.pi * r
ax = plt.subplot(111, polar=True)
ax.plot(theta, r, color='r', linewidth=3)
ax.set_rmax(2.0)
ax.grid(True)
ax.set_title("polar plot")
plt.show()
```

### 图表类型

### 直方图

```python
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)
num_bins = 50
# the histogram of the data
n, bins, patches = plt.hist(x, num_bins, normed=1,
facecolor='green', alpha=0.5)
y = mlab.normpdf(bins, mu, sigma) # add a 'best fit' line
plt.plot(bins, y, 'r--')
plt.show()
```

### 散点图

```python
import matplotlib.pyplot as plt
import numpy as np
n = 150
x = np.random.rand(n,3)
c = np.random.rand(n,3)
plt.scatter(x[:,0], x[:,1], s=x[:,2]*500, alpha=0.5, color=c)
plt.show()
```

### 柱状图

```python
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(4)
money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]
def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1fM' % (x * 1e-6)
formatter = FuncFormatter(millions)
fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
plt.bar(x, money)
plt.xticks(x, ('Bill', 'Fred', 'Mary', 'Sue'))
plt.show()
```

### 多子图

```python
• subplot(numRows, numCols, plotNum)
– plt.subplot(221) # 第一行的左图
– plt.subplot(222) # 第一行的右图
– plt.subplot(212) # 第二整行
– plt.show()
– ax1 = plt.subplot(211) # 创建子图1
– ax1.plot(x,y)
– ax2 = plt.subplot(212) # 创建子图2
– ax2.plot(x,y)
```

### colormap

```python
• 查看可用色表
import pylab as pl
pl.colormaps()
• 查看色表内容
pl.cm.hot(0.001)
pl.cm.hot(0.999)
pl.cm.hot(0.5)
pl.cm.hot(0.5, 0.5)
```

### 三维作图

```python
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax = Axes3D(fig)
data = np.random.random([100,3])
np.random.shuffle(data)
ax.scatter(data[:,0],data[:,1],data[:,2], marker='o')
plt.show()
```

### 三维曲面

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
cmap = plt.cm.jet
fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap )
ax.set_zlim(-1.01, 1.01)
plt.show()
```

### 等高线图

```python
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))
levels = np.arange(-1,1,0.25)
cs = plt.contour(X, Y, Z, levels)
plt.clabel(cs,inline=1,fontsize=8)
plt.axis('equal')
plt.show()
```

### 三维投影

```python
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_surface(X, Y, Z, rstride=8,cstride=8, alpha=0.3)
cset = ax.contour(X, Y, Z, zdir='z', offset=-100)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40)
cset = ax.contour(X, Y, Z, zdir='y', offset=40)
plt.show()
```

### mplot3d 函数

```python
• plot3D：三维控件绘图
• plot_surface： 三维网格曲面
• plot_trisurf： 三维三角曲面
• plot_wireframe：三维线图
• quiver： 矢量图
• quiver3D： 三维矢量图
• scatter: 散点图
```

### 三维球面

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b')
plt.show()
```

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.gca(projection='3d')
u, v = np.ogrid[0:2*np.pi:20j, 0:np.pi:20j]
x=np.cos(u)*np.sin(v)
y=np.sin(u)*np.sin(v)
z=np.cos(v)
ax.plot_surface(x, y, z, rstride=1, cstride=1, alpha=0.3)
plt.show()
```

### pylab实时动画

```python
import pylab as pl
import numpy as np
pl.ion() #实时绘图
pl.show()
x = np.arange(0,2*np.pi,0.01)
line, = pl.plot(x,np.sin(x))
for i in np.arange(1,200):
    line.set_ydata(np.sin(x+i/10.0))
    pl.pause(0.05)
pl.ioff() #关闭实时绘图
```

### 动画模块 animation

```python
import numpy as np  # as关键字用于创建别名。
import matplotlib.pyplot as plt
import matplotlib.animation as ani
fig = plt.figure()
x = np.arange(0, 2*np.pi, 0.01) # x-array
line, = plt.plot(x, np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10.0)) # update the data
    return line
ani.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=True)
plt.show()
```

## 解决问题

## 进阶：错误和异常

### 错误

你可以想象一个简单的 print 函数调用。如果我们把 print 误拼成 Print 会怎样？你会注意到它的首字母是大写。在这一例子中，Python 会抛出（Raise）一个语法错误。

你会注意到一个 NameError 错误被抛出，同时 Python 还会打印出检测到的错误发生的位置。这就是一个错误错误处理器（Error Handler） 为这个错误所做的事情。

### 异常

我们将尝试（Try）去读取用户的输入内容。按下 [ctrl-d] 来看看会发生什么事情。

```python
>>> s = input('Enter something --> ')
Enter something --> Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
EOFError
```

此处 Python 指出了一个称作 EOFError 的错误，代表着它发现了一个文件结尾（End of File）符号（由 ctrl-d 实现）在不该出现的时候出现了。

### 处理异常

我们可以通过使用 try..except 来处理异常状况。一般来说我们会把通常的语句放在 try 代码块中，将我们的错误处理器代码放置在 except 代码块中。

```python
try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))

#输出：
# Press ctrl + d
$ python exceptions_handle.py
Enter something --> Why did you do an EOF on me?
# Press ctrl + c
$ python exceptions_handle.py
Enter something --> ^CYou cancelled the operation.
$ python exceptions_handle.py
Enter something --> No exceptions
You entered No exceptions
```

我们将所有可能引发异常或错误的语句放在 try 代码块中，并将相应的错误或异常的处理器（Handler）放在 except 子句或代码块中。except 子句可以处理某种特定的错误或异常，或者是一个在括号中列出的错误或异常。如果没有提供错误或异常的名称，它将处理所有错误与异常。

你还可以拥有一个 else 子句与 try..except 代码块相关联。else 子句将在没有发生异常的时候执行。

### 抛出异常

你可以通过 raise 语句来引发一次异常，具体方法是提供错误名或异常名以及要抛出（Thrown）异常的对象。
你能够引发的错误或异常必须是直接或间接从属于 Exception（异常） 类的派生类。

```python
# encoding=UTF-8
class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something --> ')
    if len(text) < 3:
        #使用raise触发异常
        raise ShortInputException(len(text), 3)
    # 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

#输出:
$ python exceptions_raise.py
Enter something --> a
ShortInputException: The input was 1 long, expected at least 3
$ python exceptions_raise.py
Enter something --> abc
No exception was raised.
```

### Try ... Finally

假设你正在你的读取中读取一份文件。你应该如何确保文件对象被正确关闭，无论是否会发生异常？这可以通过 finally 块来完成。

```python
import sys
import time
f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")

#输出:
$ python exceptions_finally.py
Programming is fun
Press ctrl+c now
^C!! You cancelled the reading from the file.
(Cleaning up: Closed the file)
```

我们按照通常文件读取进行操作，但是我们同时通过使用 time.sleep 函数任意在每打印一行后插入两秒休眠，使得程序运行变得缓慢（在通常情况下 Python 运行得非常快速）。当程序在处在运行过过程中时，按下 ctrl + c 来中断或取消程序。
你会注意到 KeyboardInterrupt 异常被抛出，尔后程序退出。不过，在程序退出之前，finally 子句得到执行，文件对象总会被关闭。
另外要注意到我们在 print 之后使用了 sys.stout.flush()，以便它能被立即打印到屏幕上。

### with 语句

在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式。因此，还有一个 with 语句使得这一过程可以以一种干净的姿态得以完成。

```python
with open("poem.txt") as f:
    for line in f:
        print(line, end='')
```

程序输出的内容应与上一个案例所呈现的相同。本例的不同之处在于我们使用的是 open 函数与 with 语句——我们将关闭文件的操作交由 with open 来自动完成。
在幕后发生的事情是有一项 with 语句所使用的协议（Protocol）。它会获取由 open 语句返回的对象，在本案例中就是“thefile”。
它总会在代码块开始之前调用 thefile.__enter__ 函数，并且总会在代码块执行完毕之后调用 thefile.__exit__。
因此，我们在 finally 代码块中编写的代码应该格外留心 __exit__ 方法的自动操作。这能够帮助我们避免重复显式使用 try..finally 语句。

## 进阶：面向对象编程

类与对象是面向对象编程的两个主要方面。一个类（Class）能够创建一种新的类型（Type），其中对象（Object）就是类的实例（Instance）。可以这样来类比：你可以拥有类型 int 的变量，也就是说存储整数的变量是 int 类的实例（对象）。

对象可以使用属于它的普通变量来存储数据。这种从属于对象或类的变量叫作字段（Field）。对象还可以使用属于类的函数来实现某些功能，这种函数叫作类的方法（Method）。这两个术语很重要，它有助于我们区分函数与变量，哪些是独立的，哪些又是属于类或对象的。总之，字段与方法通称类的属性（Attribute）。
字段有两种类型——它们属于某一类的各个实例或对象，或是从属于某一类本身。它们被分别称作实例变量（Instance Variables）与类变量（Class Variables）。
通过 class 关键字可以创建一个类。这个类的字段与方法可以在缩进代码块中予以列出。

### self

类方法与普通函数只有一种特定的区别——前者必须多加一个参数在参数列表开头，这个名字必须添加到参数列表的开头，但是你不用在你调用这个功能时为这个参数赋值，Python 会为它提供。这种特定的变量引用的是对象本身，按照惯例，它被赋予 self 这一名称。
尽管你可以为这一参数赋予任何名称，但是强烈推荐你使用 self 这一名称——其它的任何一种名称绝对会引人皱眉。使用一个标准名称能带来诸多好处——任何一位你的程序的读者能够立即认出它，甚至是专门的 IDE（Integrated Development Environments，集成开发环境）也可以为你提供帮助，只要你使用了 self 这一名称。
针对 C++/Java/C# 程序员的提示Python 中的 self 相当于 C++ 中的 this 指针以及 Java 与 C# 中的 this 引用。

### 类

```python
class Person:
    pass  # 一个空的代码块

p = Person()
print(p)

#输出:
$ python oop_simplestclass.py
&lt;__main__.Person instance at 0x10171f518&gt;
```

我们通过使用 class 语句与这个类的名称来创建一个新类。在它之后是一个缩进的语句块，代表这个类的主体。在本案例中，我们创建的是一个空代码块，使用 pass 语句予以标明。
然后，我们通过采用类的名称后跟一对括号的方法，给这个类创建一个对象（或是实例，我们将在后面的章节中了解有关实例的更多内容）。为了验证我们的操作是否成功，我们通过直接将它们打印出来来确认变量的类型。结果告诉我们我们在 Person 类的 __main__ 模块中拥有了一个实例。
要注意到在本例中还会打印出计算机内存中存储你的对象的地址。案例中给出的地址会与你在你的电脑上所能看见的地址不相同，因为 Python 会在它找到的任何空间来存储对象。

### 方法

我们已经在前面讨论过类与对象一如函数那般都可以带有方法（Method），唯一的不同在于我们还拥有一个额外的 self 变量。

```python
class Person:
    def say_hi(self):
        print('Hello, how are you?')
p = Person()
p.say_hi()
# 前面两行同样可以写作
# Person().say_hi()

#输出:
$ python oop_method.py
Hello, how are you?
```

这里我们就能看见 self 是如何行动的了。要注意到 say_hi 这一方法不需要参数，但是依旧在函数定义中拥有 self 变量。

### __init__ 方法

在 Python 的类中，有不少方法的名称具有着特殊的意义。现在我们要了解的就是 __init__ 方法的意义。
__init__ 方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以对任何你想进行操作的目标对象进行初始化（Initialization）操作。这里你要注意在 init 前后加上的双下划线。

```python
class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person('Swaroop').say_hi()

#输出:
$ python oop_init.py
Hello, my name is Swaroop
```

在本例中，我们定义一个接受 name 参数（当然还有 self 参数）的 __init__ 方法。在这里，我们创建了一个字段，同样称为 name。要注意到尽管它们的名字都是“name”，但这是两个不相同的变量。虽说如此，但这并不会造成任何问题，因为 self.name 中的点号意味着这个叫作“name”的东西是某个叫作“self”的对象的一部分，而另一个 name 则是一个局部变量。由于我们已经如上这般明确指出了我们所指的是哪一个名字，所以它不会引发混乱。
当我们在 Person 类下创建新的实例 p 时，我们采用的方法是先写下类的名称，后跟括在括号中的参数，形如：p = Person('Swaroop')。
我们不会显式地调用 __init__ 方法。 这正是这个方法的特殊之处所在。
现在，我们可以使用我们方法中的 self.name 字段了，使用的方法在 say_hi 方法中已经作过说明。

### 类变量与对象变量

字段（Field）有两种类型——类变量与对象变量，它们根据究竟是类还是对象拥有这些变量来进行分类。
类变量（Class Variable）是共享的（Shared）——它们可以被属于该类的所有实例访问。该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现。
对象变量（Object variable）由类的每一个独立的对象或实例所拥有。在这种情况下，每个对象都拥有属于它自己的字段的副本，也就是说，它们不会被共享，也不会以任何方式与其它不同实例中的相同名称的字段产生关联。

```python
# coding=UTF-8
class Robot:
    """表示有一个带有名字的机器人。"""
    # 一个类变量，用来计数机器人的数量
    population = 0
    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))
        # 当有人被创建时，机器人
        # 将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了。"""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))
        
droid1 = Robot("R2-D2")     # (Initializing R2-D2)
droid1.say_hi()             # Greetings, my masters call me R2-D2.
Robot.how_many()            # We have 1 robots.

droid2 = Robot("C-3PO")     # (Initializing C-3PO)
droid2.say_hi()             # Greetings, my masters call me C-3PO.
Robot.how_many()            # We have 2 robots.

print("\nRobots can do some work here.\n")                          # Robots can do some work here.
print("Robots have finished their work. So let's destroy them.")    # Robots have finished their work. So let's destroy them.
droid1.die()                # R2-D2 is being destroyed!
                            # There are still 1 robots working.
droid2.die()                # C-3PO is being destroyed!
                            # C-3PO was the last one.
Robot.how_many()            # We have 0 robots.
```

这是一个比较长的案例，但是它有助于展现类与对象变量的本质。在本例中，population 属于 Robot 类，因此它是一个类变量。name 变量属于一个对象（通过使用 self 分配），因此它是一个对象变量。
因此，我们通过 Robot.population 而非 self.population 引用 population 类变量。我们对于 name 对象变量采用 self.name 标记法加以称呼，这是这个对象中所具有的方法。要记住这个类变量与对象变量之间的简单区别。同时你还要注意当一个对象变量与一个类变量名称相同时，类变量将会被隐藏。
除了 Robot.popluation，我们还可以使用 self.__class__.population，因为每个对象都通过 self.__class__ 属性来引用它的类。
how_many 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个 classmethod（类方法） 或是一个 staticmethod（静态方法），这取决于我们是否需要知道这一方法属于哪个类。由于我们已经引用了一个类变量，因此我们使用 classmethod（类方法）。
我们使用装饰器（Decorator）将 how_many 方法标记为类方法。
你可以将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式，因此启用 @classmethod 装饰器等价于调用：

```python
how_many = classmethod(how_many)
```

会观察到 __init__ 方法会使用一个名字以初始化 Robot 实例。在这一方法中，我们将 population 按 1 往上增长，因为我们多增加了一台机器人。你还会观察到 self.name 的值是指定给每个对象的，这体现了对象变量的本质。
你需要记住你只能使用 self 来引用同一对象的变量与方法。这被称作属性引用（Attribute Reference）。
在本程序中，我们还会看见针对类和方法的 文档字符串（DocStrings） 的使用方式。我们可以在运行时通过 Robot.__doc__ 访问类的 文档字符串，对于方法的文档字符串，则可以使用 Robot.say_hi.__doc__。
在 die 方法中，我们简单地将 Robot.population 的计数按 1 向下减少。
所有的类成员都是公开的。但有一个例外：如果你使用数据成员并在其名字中使用双下划线作为前缀，形成诸如 __privatevar 这样的形式，Python 会使用名称调整（Name-mangling）来使其有效地成为一个私有变量。
因此，你需要遵循这样的约定：任何在类或对象之中使用的变量其命名应以下划线开头，其它所有非此格式的名称都将是公开的，并可以为其它任何类或对象所使用。请记得这只是一个约定，Python 并不强制如此（除了双下划线前缀这点）。

### 继承

面向对象编程的一大优点是对代码的重用（Reuse），重用的一种实现方法就是通过继承（Inheritance）机制。继承最好是想象成在类之间实现类型与子类型（Type and Subtype）关系的工具。
现在假设你希望编写一款程序来追踪一所大学里的老师和学生。有一些特征是他们都具有的，例如姓名、年龄和地址。另外一些特征是他们独有的，一如教师的薪水、课程与假期，学生的成绩和学费。
你可以为每一种类型创建两个独立的类，并对它们进行处理。但增添一条共有特征就意味着将其添加进两个独立的类。这很快就会使程序变得笨重。
一个更好的方法是创建一个公共类叫作 SchoolMember，然后让教师和学生从这个类中继承（Inherit），也就是说他们将成为这一类型（类）的子类型，而我们就可以向这些子类型中添加某些该类独有的特征。
这种方法有诸多优点。如果我们增加或修改了 SchoolMember 的任何功能，它将自动反映在子类型中。举个例子，你可以通过简单地向 SchoolMember 类进行操作，来为所有老师与学生添加一条新的 ID 卡字段。不过，对某一子类型作出的改动并不会影响到其它子类型。另一大优点是你可以将某一老师或学生对象看作 SchoolMember 的对象并加以引用，这在某些情况下会大为有用，例如清点学校中的成员数量。这被称作多态性（Polymorphism），在任何情况下，如果父类型希望，子类型都可以被替换，也就是说，该对象可以被看作父类的实例。
同时还需要注意的是我们重用父类的代码，但我们不需要再在其它类中重复它们，当我们使用独立类型时才会必要地重复这些代码。
在上文设想的情况中，SchoolMember 类会被称作基类（Base Class）或是超类（Superclass）。Teacher 和 Student 类会被称作派生类（Derived Classes）或是子类（Subclass）。

```python
# coding=UTF-8
class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
    '''代表一位老师。'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    '''代表一位学生。'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
# 打印一行空白行
print()
members = [t, s]
for member in members:
    # 对全体师生工作
    member.tell()

#输出:

$ python oop_subclass.py
(Initialized SchoolMember: Mrs. Shrividya)
(Initialized Teacher: Mrs. Shrividya)

(Initialized SchoolMember: Swaroop)
(Initialized Student: Swaroop)

Name:"Mrs. Shrividya" Age:"40" Salary: "30000"
Name:"Swaroop" Age:"25" Marks: "75"
```
