# 流畅的 python

## 第一章 Python 数据模块

### 1.1　一摞Python风格的纸牌

```python
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
 ranks = [str(n) for n in range(2, 11)] + list('JQKA')
 suits = 'spades diamonds clubs hearts'.split() 

def __init__(self):
 self._cards = [Card(rank, suit) for suit in self.suits
 for rank in self.ranks]

 def __len__(self):
 return len(self._cards)

 def __getitem__(self, position):
 return self._cards[position]
```

首先，我们用 collections.namedtuple 构建了一个简单的类来表示一张纸牌。自 Python 2.6
开始，namedtuple 就加入到 Python 里，用以构建只有少数属性但是没有方法的对象，比如
数据库条目。如下面这个控制台会话所示，利用 namedtuple，我们可以很轻松地得到一个
纸牌对象：

```python
>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')
```

当然，我们这个例子主要还是关注 FrenchDeck 这个类，它既短小又精悍。首先，它跟任何
标准 Python 集合类型一样，可以用 len() 函数来查看一叠牌有多少张：

```python
>>> deck = FrenchDeck()
>>> len(deck)
52
```

从一叠牌中抽取特定的一张纸牌，比如说第一张或最后一张，是很容易的：deck[0] 或
deck[-1]。这都是由 __getitem__ 方法提供的：

```python
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')
```

Python 已经内置了从一个序列中随机选出一个元素的函数 random.choice

```python
>>> from random import choice
>>> choice(deck)
Card(rank='3', suit='hearts')
>>> choice(deck)
Card(rank='K', suit='spades')
>>> choice(deck)
Card(rank='2', suit='clubs')
```

现在已经可以体会到通过实现特殊方法来利用 Python 数据模型的两个好处。
• 作为你的类的用户，他们不必去记住标准操作的各式名称（“怎么得到元素的总数？
是 .size() 还是 .length() 还是别的什么？”）。
• 可以更加方便地利用Python的标准库，比如random.choice函数，从而不用重新发明轮子。

因为 __getitem__ 方法把 [] 操作交给了 self._cards 列表，所以我们的 deck 类自动支持切
片（slicing）操作。下面列出了查看一摞牌最上面 3 张和只看牌面是 A 的牌的操作。其中
第二种操作的具体方法是，先抽出索引是 12 的那张牌，然后每隔 13 张牌拿 1 张：

```python
>>> deck[:3]
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'),
Card(rank='4', suit='spades')]
>>> deck[12::13]    #从12开始，每隔13张牌取一张 deck[12]  deck[12+13] ......    先抽出索引是 12 的那张牌，然后每隔 13 张牌拿 1 张
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'),
Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
```

另外，仅仅实现了 __getitem__ 方法，这一摞牌就变成可迭代的了：

```python
>>> for card in deck: # doctest: +ELLIPSIS
... print(card)
Card(rank='2', suit='spades')
Card(rank='3', suit='spades')
Card(rank='4', suit='spades')
...

#反向迭代也没关系：
>>> for card in reversed(deck): # doctest: +ELLIPSIS
... print(card)
Card(rank='A', suit='hearts')
Card(rank='K', suit='hearts')
Card(rank='Q', suit='hearts')
...
```

```python
doctest 中的省略
为了尽可能保证书中的 Python 控制台会话内容的正确性，这些内容都是直
接从 doctest 里摘录的。在测试中，如果可能的输出过长的话，那么过长的
内容就会被如上面例子的最后一行的省略号（...）所替代。此时就需要
#doctest: +ELLIPSIS 这个指令来保证 doctest 能够通过。要是你自己照着书
中例子在控制台中敲代码，可以略过这一指令。
```

迭代通常是隐式的，譬如说一个集合类型没有实现 __contains__ 方法，那么 in 运算符就
会按顺序做一次迭代搜索。于是，in 运算符可以用在我们的 FrenchDeck 类上，因为它是
可迭代的：

```python
>>> Card('Q', 'hearts') in deck
True
>>> Card('7', 'beasts') in deck
False
```

那么排序呢？我们按照常规，用点数来判定扑克牌的大小，2 最小、A 最大；同时还要加
上对花色的判定，黑桃最大、红桃次之、方块再次、梅花最小。下面就是按照这个规则来
给扑克牌排序的函数，梅花 2 的大小是 0，黑桃 A 是 51：

```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
 rank_value = FrenchDeck.ranks.index(card.rank)
 return rank_value * len(suit_values) + suit_values[card.suit]
```

有了 spades_high 函数，就能对这摞牌进行升序排序了：

```python
>>> for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
... print(card)
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
... (46 cards ommitted)
Card(rank='A', suit='diamonds')
Card(rank='A', suit='hearts')
Card(rank='A', suit='spades')
```

虽然 FrenchDeck 隐式地继承了 object 类，5 但功能却不是继承而来的。我们通过数据模型和
一些合成来实现这些功能。通过实现 __len__ 和 __getitem__ 这两个特殊方法，FrenchDeck
就跟一个 Python 自有的序列数据类型一样，可以体现出 Python 的核心语言特性（例如迭
代和切片）。同时这个类还可以用于标准库中诸如 random.choice、reversed 和 sorted 这
些函数。另外，对合成的运用使得 __len__ 和 __getitem__ 的具体实现可以代理给 self.
_cards 这个 Python 列表（即 list 对象）。

### 1.2　如何使用特殊方法

首先明确一点，特殊方法的存在是为了被 Python 解释器调用的，你自己并不需要调用它
们。也就是说没有 my_object.__len__() 这种写法，而应该使用 len(my_object)。在执行
len(my_object) 的时候，如果 my_object 是一个自定义类的对象，那么 Python 会自己去调
用其中由你实现的 __len__ 方法。

### 1.2.1　模拟数值类型

一个二维向量加法的例子，Vector(2,4) + Vextor(2,1) = Vector(4,5)

为了给这个类设计 API，我们先写个模拟的控制台会话来做 doctest。下面这一段代码就是
图 1-1 所示的向量加法：

```python
>>> v1 = Vector(2, 4)
>>> v2 = Vector(2, 1)
>>> v1 + v2
Vector(4, 5)
```

注意其中的 + 运算符所得到的结果也是一个向量，而且结果能被控制台友好地打印出来。

abs 是一个内置函数，如果输入是整数或者浮点数，它返回的是输入值的绝对值；如果输
入是复数（complex number），那么返回这个复数的模。为了保持一致性，我们的 API 在碰
到 abs 函数的时候，也应该返回该向量的模：

```python
>>> v = Vector(3, 4)
>>> abs(v)
5.0
```

我们还可以利用 * 运算符来实现向量的标量乘法（即向量与数的乘法，得到的结果向量的
方向与原向量一致 6
，模变大）：

```python
>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0
```

示例 1-2 包含了一个 Vector 类的实现，上面提到的操作在代码里是用这些特殊方法实现
的：__repr__、__abs__、__add__ 和 __mul_

示例 1-2　一个简单的二维向量类:

```python
from math import hypot
class Vector:
 def __init__(self, x=0, y=0):
 self.x = x
 self.y = y
 def __repr__(self):
 return 'Vector(%r, %r)' % (self.x, self.y)
 def __abs__(self):
 return hypot(self.x, self.y)
 def __bool__(self):
 return bool(abs(self))
 def __add__(self, other):
 x = self.x + other.x
 y = self.y + other.y
 return Vector(x, y)
 def __mul__(self, scalar):
 return Vector(self.x * scalar, self.y * scalar)
```

### 1.2.2　字符串表示形式

```python
Python 有一个内置的函数叫 repr，它能把一个对象用字符串的形式表达出来以便辨认，这
就是“字符串表示形式”。repr 就是通过 __repr__ 这个特殊方法来得到一个对象的字符串
表示形式的。如果没有实现 __repr__，当我们在控制台里打印一个向量的实例时，得到的
字符串可能会是 <Vector object at 0x10e100070>。
交互式控制台和调试程序（debugger）用 repr 函数来获取字符串表示形式；在老的使用 %
符号的字符串格式中，这个函数返回的结果用来代替 %r 所代表的对象；同样，str.format
函数所用到的新式字符串格式化语法（https://docs.python.org/2/library/string.html#formatstring-syntax）也是利用了 repr，才把 !r 字段变成字符串。
% 和 str.format 这两种格式化字符串的手段在本书中都会使用。其实整个
Python 社区都在同时使用这两种方法。个人来讲，我越来越喜欢 str.format
了，但是 Python 程序员更喜欢简单的 %。因此，这两种形式并存的情况还会
持续下去。
在 __repr__ 的实现中，我们用到了 %r 来获取对象各个属性的标准字符串表示形式——这
是个好习惯，它暗示了一个关键：Vector(1, 2) 和 Vector('1', '2') 是不一样的，后者在
我们的定义中会报错，因为向量对象的构造函数只接受数值，不接受字符串 7
。
__repr__ 所返回的字符串应该准确、无歧义，并且尽可能表达出如何用代码创建出这个被
打印的对象。因此这里使用了类似调用对象构造器的表达形式（比如 Vector(3, 4) 就是个
例子）。
__repr__ 和 __str__ 的区别在于，后者是在 str() 函数被使用，或是在用 print 函数打印
一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。
如果你只想实现这两个特殊方法中的一个，__repr__ 是更好的选择，因为如果一个对象没
有 __str__ 函数，而 Python 又需要调用它的时候，解释器会用 __repr__ 作为替代。
“Difference between __str__ and __repr__ in Python”（http://stackoverflow.com/
questions/1436703/difference-between-str-and-repr-in-python）是 Stack Overflow 上
的一个问题，Python 程序员 Alex Martelli 和 Martijn Pieters 的回答很精彩。

```

### 1.2.3　算术运算符

通过 __add__ 和 __mul__，示例 1-2 为向量类带来了 + 和 * 这两个算术运算符。值得注意的
是，这两个方法的返回值都是新创建的向量对象，被操作的两个向量（self 或 other）还
是原封不动，代码里只是读取了它们的值而已。中缀运算符的基本原则就是不改变操作对
象，而是产出一个新的值。第 13 章会谈到更多这方面的问题。

### 1.2.4　自定义的布尔值

```python
尽管 Python 里有 bool 类型，但实际上任何对象都可以用于需要布尔值的上下文中（比如
if 或 while 语句，或者 and、or 和 not 运算符）。为了判定一个值 x 为真还是为假，Python
会调用 bool(x)，这个函数只能返回 True 或者 False。
默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对 __bool__ 或者 __
len__ 函数有自己的实现。bool(x) 的背后是调用 x.__bool__() 的结果；如果不存在 __
bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()。若返回 0，则 bool 会返回 False；否
则返回 True。
我们对 __bool__ 的实现很简单，如果一个向量的模是 0，那么就返回 False，其他情况则
返回 True。因为 __bool__ 函数的返回类型应该是布尔型，所以我们通过 bool(abs(self))
把模值变成了布尔值。
在 Python 标准库的文档中，有一节叫作“Built-in Types”（https://docs.python.org/3/library/
stdtypes.html#truth），其中规定了真值检验的标准。通过实现 __bool__，你定义的对象就可
以与这个标准保持一致。
```

```python
如果想让 Vector.__bool__ 更高效，可以采用这种实现：
def __bool__(self):
 return bool(self.x or self.y)
它不那么易读，却能省掉从 abs 到 __abs__ 到平方再到平方根这些中间步骤。
通过 bool 把返回类型显式转换为布尔值是为了符合 __bool__ 对返回值的规
定，因为 or 运算符可能会返回 x 或者 y 本身的值：若 x 的值等价于真，则
or 返回 x 的值；否则返回 y 的值。
```

### 1.3　特殊方法一览

```python
#表1-1：跟运算符无关的特殊方法
类别            方法名
字符串 / 字节序列
　表示形式      __repr__、__str__、__format__、__bytes__
数值转换        __abs__、__bool__、__complex__、__int__、__float__、__hash__、__index__
集合模拟        __len__、__getitem__、__setitem__、__delitem__、__contains__
迭代枚举        __iter__、__reversed__、__next__
可调用模拟      __call__
上下文管理      __enter__、__exit__
实例创建和销毁  __new__、__init__、__del__
属性管理        __getattr__、__getattribute__、__setattr__、__delattr__、__dir__
属性描述符      __get__、__set__、__delete__
跟类相关的服务  __prepare__、__instancecheck__、__subclasscheck__

```

```python
#表1-2：跟运算符相关的特殊方法
类别            方法名和对应的运算符
一元运算符          __neg__ -、__pos__ +、__abs__ abs()
众多比较运算符      __lt__ <、__le__ <=、__eq__ ==、__ne__ !=、__gt__ >、__ge__ >=
算术运算符          __add__ +、__sub__ -、__mul__ *、__truediv__ /、__floordiv__ //、__mod__ %、__divmod__ divmod()、__pow__ ** 或 pow()、__round__ round()
反向算术运算符      __radd__、__rsub__、__rmul__、__rtruediv__、__rfloordiv__、__rmod__、__rdivmod__、__rpow__
增量赋值算术运算符  __iadd__、__isub__、__imul__、__itruediv__、__ifloordiv__、__imod__、__ipow__
位运算符            __invert__ ~、__lshift__ <<、__rshift__ >>、__and__ &、__or__ |、__xor__ ^
反向位运算符        __rlshift__、__rrshift__、__rand__、__rxor__、__ror__
增量赋值位运算符    __ilshift__、__irshift__、__iand__、__ixor__、__ior__
```

```python
当交换两个操作数的位置时，就会调用反向运算符（b * a 而不是 a * b）。
增量赋值运算符则是一种把中缀运算符变成赋值运算的捷径（a = a * b 就
变成了 a *= b）。第 13 章会对这两者作出详细解释。
```

### 1.4　为什么len不是普通方法

我在 2013 年问核心开发者 Raymond Hettinger 这个问题时，他用“Python 之禅”（https://
www.python.org/doc/humor/#the-zen-of-python）里的原话回答了我：“实用胜于纯粹。”在
1.2 节里我提到过，如果 x 是一个内置类型的实例，那么 len(x) 的速度会非常快。背后的
原因是 CPython 会直接从一个 C 结构体里读取对象的长度，完全不会调用任何方法。获取
一个集合中元素的数量是一个很常见的操作，在 str、list、memoryview 等类型上，这个
操作必须高效。
换句话说，len 之所以不是一个普通方法，是为了让 Python 自带的数据结构可以走后门，
abs 也是同理。但是多亏了它是特殊方法，我们也可以把 len 用于自定义数据类型。这种
处理方式在保持内置类型的效率和保证语言的一致性之间找到了一个平衡点，也印证了
“Python 之禅”中的另外一句话：“不能让特例特殊到开始破坏既定规则。”
如果把 abs 和 len 都看作一元运算符的话，你也许更能接受它们——虽然看
起来像面向对象语言中的函数，但实际上又不是函数。有一门叫作 ABC 的
语言是 Python 的直系祖先，它内置了一个 # 运算符，当你写出 #s 的时候，
它的作用跟 len 一样。如果写成 x#s 这样的中缀运算符的话，那么它的作用
是计算 s 中 x 出现的次数。在 Python 里对应的写法是 s.count(x)。注意这里
的 s 是一个序列类型。

## 第 2 章序列构成的数组

### 2.1　内置序列类型概览

容器序列
list、tuple 和 collections.deque 这些序列能存放不同类型的数据。
扁平序列

str、bytes、bytearray、memoryview 和 array.array，这类序列只能容纳一种类型.

容器序列存放的是它们所包含的任意类型的对象的引用，而扁平序列里存放的是值而不是
引用。(只能存放诸如字符、字节和数值这种基础类型)

可变序列
list、bytearray、array.array、collections.deque 和 memoryview。

不可变序列
tuple、str 和 bytes。

### 2.2　列表推导和生成器表达式

#### 2.2.1　列表推导和可读性

```python
#示例 2-1　把一个字符串变成 Unicode 码位的列表
>>> symbols = '$¢£¥€¤'
>>> codes = []
>>> for symbol in symbols:
... codes.append(ord(symbol)) #从给定的字符值中获取数字值（获取ASCII值）
...
>>> codes
[36, 162, 163, 165, 8364, 164]
```

```python
#示例 2-2　把字符串变成 Unicode 码位的另外一种写法
>>> symbols = '$¢£¥€¤'
>>> codes = [ord(symbol) for symbol in symbols]     #从给定的字符值中获取数字值（获取ASCII值）
>>> codes
[36, 162, 163, 165, 8364, 164]
```

#### 2.2.2　列表推导同filter和map的比较

```python
示例 2-3　用列表推导和 map/filter 组合来创建同样的表单
>>> symbols = '$¢£¥€¤'
>>> beyond_ascii = [ord(s) for s in symbols if ord(s) > 127] #ord(s)  [36, 162, 163, 165, 8364, 164]
>>> beyond_ascii
[162, 163, 165, 8364, 164]
>>> beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))   #filter过滤     map() 会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
>>> beyond_ascii
[162, 163, 165, 8364, 164]
```

#### 2.2.3　笛卡儿积

含有 4 种花色和 3 种牌面的列表的笛卡儿积，结果是一个包含 12 个元素的列表

```python
示例 2-4　使用列表推导计算笛卡儿积
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors for size in sizes] ➊
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
 ('white', 'M'), ('white', 'L')]
>>> for color in colors: ➋
... for size in sizes:
... print((color, size))
...
('black', 'S')
('black', 'M')
('black', 'L')
('white', 'S')
('white', 'M')
('white', 'L')
>>> tshirts = [(color, size) for size in sizes ➌
... for color in colors]
>>> tshirts
[('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
 ('black', 'L'), ('white', 'L')]
```

➊ 这里得到的结果是先以颜色排列，再以尺码排列。
➋ 注意，这里两个循环的嵌套关系和上面列表推导中 for 从句的先后顺序一样。
➌ 如果想依照先尺码后颜色的顺序来排列，只需要调整从句的顺序。我在这里插入了一个
换行符，这样顺序安排就更明显了。

#### 2.2.4　生成器表达式

生成器表达式的语法跟列表推导差不多，只不过把方括号换成圆括号而已。

```python
#示例 2-5　用生成器表达式初始化元组和数组
>>> symbols = '$¢£¥€¤'
>>> tuple(ord(symbol) for symbol in symbols) ➊
(36, 162, 163, 165, 8364, 164)
>>> import array
>>> array.array('I', (ord(symbol) for symbol in symbols)) ➋
array('I', [36, 162, 163, 165, 8364, 164])
➊ 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围
起来。
➋ array 的构造方法需要两个参数，因此括号是必需的。array 构造方法的第一个参数指
定了数组中数字的存储方式。
```

```python
#示例 2-6　使用生成器表达式计算笛卡儿积
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes): ➊
... print(tshirt)
...
black S
black M
black L
white S
white M
white L
➊ 生成器表达式逐个产出元素，从来不会一次性产出一个含有 6 个 T 恤样式的列表。
```

### 2.3　元组不仅仅是不可变的列表

#### 2.3.1　元组和记录

```python
示例 2-7　把元组用作记录
>>> lax_coordinates = (33.9425, -118.408056) ➊
>>> city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014) ➋
>>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ➌
... ('ESP', 'XDA205856')]
>>> for passport in sorted(traveler_ids): ➍
... print('%s/%s' % passport) ➎
...
BRA/CE342567
ESP/XDA205856
USA/31195855
>>> for country, _ in traveler_ids: ➏
... print(country)
...
USA
BRA
ES
➊ 洛杉矶国际机场的经纬度。
➋ 东京市的一些信息：市名、年份、人口（单位：百万）、人口变化（单位：百分比）和
面积（单位：平方千米）。
➌ 一个元组列表，元组的形式为 (country_code, passport_number)。
➍ 在迭代的过程中，passport 变量被绑定到每个元组上。
➎ % 格式运算符能被匹配到对应的元组元素上。
➏ for 循环可以分别提取元组里的元素，也叫作拆包（unpacking）。因为元组中第二个元
素对我们没有什么用，所以它赋值给“_”占位符。
```

#### 2.3.2　元组拆包

而这所有的赋值我们只用一行声明就写完了。同样，在后
面一行中，一个 % 运算符就把 passport 元组里的元素对应到了 print 函数的格式字符串空档中。这两个都是对元组拆包的应用。

```python
>>> lax_coordinates = (33.9425, -118.408056)
>>> latitude, longitude = lax_coordinates # 元组拆包
>>> latitude
33.9425
>>> longitude
-118.408056
```

```python
>>> divmod(20, 8)   #divmod()返回一个包含商和余数的元组
(2, 4)
>>> t = (20, 8)
>>> divmod(*t)
(2, 4)
>>> quotient, remainder = divmod(*t)
>>> quotient, remainder
(2, 4)
```

os.path.split() 函数返回以路径和最后一个文件名组成的元组 (path, last_part)

```python
>>> import os
>>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
>>> filename
'idrsa.pub
```

拆包的时候，我们不总是对元组里所有的数据都感兴趣，_ 占位符能帮助处理这种情况.

元组拆包中使用 * 也可以帮助我们把注意力集中在元组的部分元素上

```python
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
>>> a, b, *rest = range(3)
>>> a, b, rest
(0, 1, [2])
>>> a, b, *rest = range(2)
>>> a, b, rest
(0, 1, [])
```

```python
>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
>>> *head, b, c, d = range(5)
>>> head, b, c, d
([0, 1], 2, 3, 4)
```

#### 2.3.3　嵌套元组拆包

元组可以是嵌套式的，例如 (a, b, (c, d))。

```python
示例 2-8　用嵌套元组来获取经度
metro_areas = [
 ('Tokyo','JP',36.933,(35.689722,139.691667)), # ➊
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas: # ➋
 if longitude <= 0: # ➌
 print(fmt.format(name, latitude, longitude))
➊ 每个元组内有 4 个元素，其中最后一个元素是一对坐标。
➋ 我们把输入元组的最后一个元素拆包到由变量构成的元组里，这样就获取了坐标。
➌ if longitude <= 0: 这个条件判断把输出限制在西半球的城市。

#示例 2-8 的输出是这样的：
                | lat.     | long.
Mexico City     | 19.4333  | -99.1333
New York-Newark | 40.8086  | -74.0204
Sao Paul        | -23.5478 | -46.6358
```

#### 2.3.4　具名元组

collections.namedtuple 是一个工厂函数，它可以用来构建一个带字段名的元组和一个有名字的类——这个带名字的类对调试程序有很大帮助

```python
在第 1 章的示例 1-1 中是这样新建 Card 类的：
Card = collections.namedtuple('Card', ['rank', 'suit'])
```

```python
#示例 2-9　定义和使用具名元组
>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates') ➊
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667)) ➋
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
139.691667))
>>> tokyo.population ➌
36.933
>>> tokyo.coordinates
(35.689722, 139.691667)
>>> tokyo[1]
'JP'
➊ 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可
以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
➋ 存放在对应字段里的数据要以一串参数的形式传入到构造函数中（注意，元组的构造函
数却只接受单一的可迭代对象）。
➌ 你可以通过字段名或者位置来获取一个字段的信息
```

```python
#示例 2-10　具名元组的属性和方法（接续前一个示例）
>>> City._fields ➊
('name', 'country', 'population', 'coordinates')
>>> LatLong = namedtuple('LatLong', 'lat long')
>>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
>>> delhi = City._make(delhi_data) ➋
>>> delhi._asdict() ➌
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population',
21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
>>> for key, value in delhi._asdict().items():
 print(key + ':', value)
name: Delhi NCR
country: IN
population: 21.935
coordinates: LatLong(lat=28.613889, long=77.208889)
>>>
➊ _fields 属性是一个包含这个类所有字段名称的元组。
➋ 用 _make() 通 过 接 受 一 个 可 迭 代 对 象 来 生 成 这 个 类 的 一 个 实 例， 它 的 作 用 跟
City(*delhi_data) 是一样的。
➌ _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元
组里的信息友好地呈现出来。
```

### 2.4　切片

列表（list）、元组（tuple）和字符串（str）这类序列类型都支持切片操作

#### 2.4.1　为什么切片和区间会忽略最后一个元素

Python、C 和其他语言里以 0 作为起始下标的传统

```python
list[:x] 和 my_list[x:] 就可以了，如下所示。
>>> l = [10, 20, 30, 40, 50, 60]
>>> l[:2] # 在下标2的地方分割
[10, 20]
>>> l[2:]
[30, 40, 50, 60]
>>> l[:3] # 在下标3的地方分割
[10, 20, 30]
 >>> l[3:]
[40, 50, 60
```

#### 2.4.2　对对象进行切片

s[a:b:c] 的形式对 s 在 a 和 b 之间以 c 为间隔取值。c 的值还可以为负，负值意味着反向取值.

```python
>>> s = 'bicycle'
>>> s[::3]
'bye'
>>> s[::-1]
'elcycib'
>>> s[::-2]
'eccb'
```

seq[start:stop:step]进 行 求 值 的 时 候，Python 会调用 seq.__getitem__(slice(start, stop, step))

```python
示例 2-11 纯文本文件形式的收据以一行字符串的形式被解析
>>> invoice = """
... 0.....6................................40........52...55........
... 1909 Pimoroni PiBrella $17.50 3 $52.50
... 1489 6mm Tactile Switch x20 $4.95 2 $9.90
... 1510 Panavise Jr. - PV-201 $28.00 1 $28.00
... 1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
... """
>>> SKU = slice(0, 6)
>>> DESCRIPTION = slice(6, 40)
>>> UNIT_PRICE = slice(40, 52)
>>> QUANTITY = slice(52, 55)
>>> ITEM_TOTAL = slice(55, None)
>>> line_items = invoice.split('\n')[2:]
>>> for item in line_items:
... print(item[UNIT_PRICE], item[DESCRIPTION])
...
 $17.50 Pimoroni PiBrella
 $4.95 6mm Tactile Switch x20
 $28.00 Panavise Jr. - PV-201
 $34.95 PiTFT Mini Kit 320x240
```

#### 2.4.4　给切片赋值

```python
>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[2:5] = [20, 30]
>>> l
[0, 1, 20, 30, 5, 6, 7, 8, 9]
>>> del l[5:7]
>>> l
[0, 1, 20, 30, 5, 8, 9]
>>> l[3::2] = [11, 22]
>>> l
[0, 1, 20, 11, 5, 22, 9]
>>> l[2:5] = 100 ➊
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> l[2:5] = [100]
>>> l
[0, 1, 100, 22, 9]
 ➊如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象。即便只有单独
一个值，也要把它转换成可迭代的序列。
```

### 2.5　对序列使用+和*

Python 程序员会默认序列是支持 + 和 * 操作的

```python
>>> l = [1, 2, 3]
>>> l * 5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> 5 * 'abcd'
'abcdabcdabcdabcdabcd'
```

+ 和 * 都遵循这个规律，不修改原有的操作对象，而是构建一个全新的序列。

```python
#建立由列表组成的列表
#示例 2-12 一个包含 3 个列表的列表，嵌套的 3 个列表各自有 3 个元素来代表井字游戏的一行方块

>>> board = [['_'] * 3 for i in range(3)] ➊
>>> board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
>>> board[1][2] = 'X' ➋
>>> board
[['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
➊ 建立一个包含 3 个列表的列表，被包含的 3 个列表各自有 3 个元素。打印出这个嵌套列表。
➋ 把第 1 行第 2 列的元素标记为 X，再打印出这个列表。
```

```python
#示例 2-13 含有 3 个指向同一对象的引用的列表是毫无用处的
>>> weird_board = [['_'] * 3] * 3 ➊
>>> weird_board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
>>> weird_board[1][2] = 'O' ➋
>>> weird_board
[['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
➊ 外面的列表其实包含 3 个指向同一个列表的引用。当我们不做修改的时候，看起来都
还好。
➋ 一旦我们试图标记第 1 行第 2 列的元素，就立马暴露了列表内的 3 个引用指向同一个对
象的事实。
```

```python
#示例 2-13 犯的错误本质上跟下面的代码犯的错误一样：
row=['_'] * 3
board = []
for i in range(3):
    board.append(row) ➊
➊ 追加同一个行对象（row）3 次到游戏板（board）。
#相反，示例 2-12 中的方法等同于这样做：
>>> board = []
>>> for i in range(3):
... row=['_'] * 3 # ➊
... board.append(row)
...
>>> board
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
>>> board[2][0] = 'X'
>>> board # ➋
[['_', '_', '_'], ['_', '_', '_'], ['X', '_', '_']]
➊ 每次迭代中都新建了一个列表，作为新的一行（row）追加到游戏板（board）。
➋ 正如我们所期待的，只有第 2 行的元素被修改。
```

### 2.6　序列的增量赋值

+= 背后的特殊方法是 __iadd__（用于“就地加法”）。但是如果一个类没有实现这个方法的话，Python 会退一步调用 __add__。

`>>> a += b`

如 果 a 实现了 __iadd__ 方 法， 就 会 调 用 这 个 方 法， 同 时 对 可 变 序 列（ 例 如 list、
bytearray 和 array.array）来说a 会就地改动，就像调用了 a.extend(b) 一样。但是如
果 a 没有实现 __iadd__ 的话，a += b 这个表达式的效果就变得跟 a = a + b 一样了：首先
计算 a + b，得到一个新的对象，然后赋值给 a

```python
*= 在可变和不可变序列上的作用：
>>> l = [1, 2, 3]
>>> id(l)
4311953800 ➊
>>> l *= 2
>>> l
[1, 2, 3, 1, 2, 3]
>>> id(l)
4311953800 ➋
>>> t = (1, 2, 3)
>>> id(t)
4312681568 ➌
>>> t *= 2
>>> id(t)
4301348296 ➍
➊ 刚开始时列表的 ID。
➋ 运用增量乘法后，列表的 ID 没变，新元素追加到列表上。
➌ 元组最开始的 ID。
➍ 运用增量乘法后，新的元组被创建。
```

```python
#一个关于+=的谜题
示例 2-14 一个谜题
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
到底会发生下面 4 种情况中的哪一种？
a. t 变成 (1, 2, [30, 40, 50, 60])。
b. 因为 tuple 不支持对它的元素赋值，所以会抛出 TypeError 异常。
c. 以上两个都不是。
d. a 和 b 都是对的。

但其实答案是 d，也就是说 a 和 b 都是对的！
```

```python
#示例 2-15 没人料到的结果：t[2] 被改动了，但是也有异常抛出
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
```

如果写成 t[2].extend([50, 60]) 就能避免这个异常

```python
#示例 2-16 s[a] = b 背后的字节码
>>> dis.dis('s[a] += b')
 1 0 LOAD_NAME 0(s)
 3 LOAD_NAME 1(a)
 6 DUP_TOP_TWO
 7 BINARY_SUBSCR ➊
 8 LOAD_NAME 2(b)
 11 INPLACE_ADD ➋
 12 ROT_THREE
 13 STORE_SUBSCR ➌
 14 LOAD_CONST 0(None)
 17 RETURN_VALUE

➊ 将 s[a] 的值存入 TOS（Top Of Stack，栈的顶端）。
➋ 计算 TOS += b。这一步能够完成，是因为 TOS 指向的是一个可变对象（也就是示例 2-15
里的列表）。
➌ s[a] = TOS 赋值。这一步失败，是因为 s 是不可变的元组（示例 2-15 中的元组 t）。
```

### 2.7 list.sort方法和内置函数sorted

list.sort 方法会就地排序列表，也就是说不会把原列表复制一份,Python 的一个惯例：如果一个函数或者方法对对象进行的是就地改动，那它就应该返回
None，好让调用者知道传入的参数发生了变动，而且并未产生新的对象。

与 list.sort 相反的是内置函数 sorted，它会新建一个列表作为返回值。这个方法可以接
受任何形式的可迭代对象作为参数，甚至包括不可变序列或生成器而不管sorted 接受的是怎样的参数，它最后都会返回一个列表。

list.sort 方法 sorted 函数，都有两个可选的关键字参数。
reverse
如果被设定为 True，被排序的序列里的元素会以降序输出,这个参数的默认值是 False。
key
在对一些字符串排序时，可以用 key=str.lower 来实现忽略大小写的排序,
或者用 key=len 进行基于字符串长度的排序

```python
>>> fruits = ['grape', 'raspberry', 'apple', 'banana']
>>> sorted(fruits)
['apple', 'banana', 'grape', 'raspberry'] ➊
>>> fruits
['grape', 'raspberry', 'apple', 'banana'] ➋
>>> sorted(fruits, reverse=True)
['raspberry', 'grape', 'banana', 'apple'] ➌
>>> sorted(fruits, key=len)
['grape', 'apple', 'banana', 'raspberry'] ➍
>>> sorted(fruits, key=len, reverse=True)
['raspberry', 'banana', 'grape', 'apple'] ➎
>>> fruits
['grape', 'raspberry', 'apple', 'banana'] ➏
>>> fruits.sort() ➐
>>> fruits
['apple', 'banana', 'grape', 'raspberry'] ➑
➊ 新建了一个按照字母排序的字符串列表。
➋ 原列表并没有变化。
➌ 按照字母降序排序。
➍ 新建一个按照长度排序的字符串列表。因为这个排序算法是稳定的，grape 和 apple 的
长度都是 5，它们的相对位置跟在原来的列表里是一样的。
➎ 按照长度降序排序的结果。结果并不是上面那个结果的完全翻转，因为用到的排序算法
是稳定的，也就是说在长度一样时，grape 和 apple 的相对位置不会改变。
➏ 直到这一步，原列表 fruits 都没有任何变化。
➐ 对原列表就地排序，返回值 None 会被控制台忽略。
➑ 此时 fruits 本身被排序。
```

### 2.8　用bisect来管理已排序的序列

bisect 模块包含两个主要函数，bisect 和 insort，两个函数都利用二分查找算法来在有序
序列中查找或插入元素。

#### 2.8.1　用bisect来搜索

bisect(haystack, needle) 在 haystack（干草垛）里搜索 needle（针）的位置，该位置满
足的条件是，把 needle 插入这个位置之后，haystack 还能保持升序。也就是在说这个函
数返回的位置前面的值，都小于或等于 needle 的值

```python
#示例 2-17 在有序序列中用 bisect 查找某个元素的插入位置
import bisect
import sys
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'
def demo(bisect_fn):
 for needle in reversed(NEEDLES):
 position = bisect_fn(HAYSTACK, needle) ➊
 offset = position * ' |' ➋
 print(ROW_FMT.format(needle, position, offset)) ➌
if __name__ == '__main__':
 if sys.argv[-1] == 'left': ➍
 bisect_fn = bisect.bisect_left
 else:
 bisect_fn = bisect.bisect
 print('DEMO:', bisect_fn.__name__) ➎
 print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
 demo(bisect_fn)
➊ 用特定的 bisect 函数来计算元素应该出现的位置。
➋ 利用该位置来算出需要几个分隔符号。
➌ 把元素和其应该出现的位置打印出来。
➍ 根据命令上最后一个参数来选用 bisect 函数。
➎ 把选定的函数在抬头打印出来。
```

bisect 的表现可以从两个方面来调教。
首先可以用它的两个可选参数——lo 和 hi——来缩小搜寻的范围。lo 的默认值是 0，hi
的默认值是序列的长度，即 len() 作用于该序列的返回值。

bisect 函数其实是 bisect_right 函数的别名，后者还有个姊妹函数叫 bisect_left。

bisect_left 返回的插入位置是原序列中跟被插入元素相等的元素的位置，也就是新元素会被放置于它相等的元素的前面，而 bisect_right 返回的则是跟它相等的元素之后的位置。这个细微的差别可能对于整数序列来讲没什么用，但是对于那些值相等但是形式不同的数据类型来讲，结果就不一样了。比如说虽然 1 == 1.0 的返回值是 True，1 和 1.0其实是两个不同的元素。

bisect 可以用来建立一个用数字作为索引的查询表格，比如说把分数和成绩 8 对应起来

```python
#示例 2-18 根据一个分数，找到它所对应的成绩
>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
... i = bisect.bisect(breakpoints, score)
... return grades[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

#### 2.8.2　用bisect.insort插入新元素

排序很耗时，因此在得到一个有序序列之后，我们最好能够保持它的有序。bisect.insort就是为了这个而存在的。

insort(seq, item) 把变量 item 插入到序列 seq 中，并能保持 seq 的升序顺序。

```python
示例 2-19 insort 可以保持有序序列的顺序
import bisect
import random
SIZE=7
random.seed(1729)
my_list = []
for i in range(SIZE):
 new_item = random.randrange(SIZE*2)
 bisect.insort(my_list, new_item)
 print('%2d ->' % new_item, my_list)
```

insort 跟 bisect 一样，有 lo 和 hi 两个可选参数用来控制查找的范围。它也有个变体叫insort_left，这个变体在背后用的是 bisect_left。

### 2.9　当列表不是首选时

#### 2.9.1　数组

如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效。数组支持所有跟
可变序列有关的操作，包括 .pop、.insert 和 .extend。
数组还提供从文件读取和存入文件的更快的方法，如 .frombytes 和 .tofile

```python
#示例 2-20 一个浮点型数组的创建、存入文件和从文件读取的过程
>>> from array import array ➊
>>> from random import random
>>> floats = array('d', (random() for i in range(10**7))) ➋
>>> floats[-1] ➌
0.07802343889111107
>>> fp = open('floats.bin', 'wb')
>>> floats.tofile(fp) ➍
>>> fp.close()
>>> floats2 = array('d') ➎
>>> fp = open('floats.bin', 'rb')
>>> floats2.fromfile(fp, 10**7) ➏
>>> fp.close()
>>> floats2[-1] ➐
0.07802343889111107
>>> floats2 == floats ➑
True
➊ 引入 array 类型。
➋ 利用一个可迭代对象来建立一个双精度浮点数组（类型码是 'd'），这里我们用的可迭
代对象是一个生成器表达式。
➌ 查看数组的最后一个元素。
➍ 把数组存入一个二进制文件里。
➎ 新建一个双精度浮点空数组。
➏ 把 1000 万个浮点数从二进制文件里读取出来。
➐ 查看新数组的最后一个元素。
➑ 检查两个数组的内容是不是完全一样。
```

#### 2.9.2　内存视图

memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片

```python
示例 2-21 通过改变数组中的一个字节来更新数组里某个元素的值
>>> numbers = array.array('h', [-2, -1, 0, 1, 2])
>>> memv = memoryview(numbers) ➊
>>> len(memv)
5
>>> memv[0] ➋
-2
>>> memv_oct = memv.cast('B') ➌
>>> memv_oct.tolist() ➍
[254, 255, 255, 255, 0, 0, 1, 0, 2, 0]
>>> memv_oct[5] = 4 ➎
>>> numbers
array('h', [-2, -1, 1024, 1, 2]) ➏
➊ 利用含有 5 个短整型有符号整数的数组（类型码是 'h'）创建一个 memoryview。
➋ memv 里的 5 个元素跟数组里的没有区别。
➌ 创建一个 memv_oct，这一次是把 memv 里的内容转换成 'B' 类型，也就是无符号字符。
➍ 以列表的形式查看 memv_oct 的内容。
➎ 把位于位置 5 的字节赋值成 4。
➏ 因为我们把占 2 个字节的整数的高位字节改成了 4，所以这个有符号整数的值就变成
了 1024。
```

#### 2.9.3 NumPy和SciPy

```python
示例 2-22 对 numpy.ndarray 的行和列进行基本操作
>>> import numpy ➊
>>> a = numpy.arange(12) ➋
>>> a
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
>>> type(a)
<class 'numpy.ndarray'>
>>> a.shape ➌
(12,)
>>> a.shape = 3, 4 ➍
>>> a
array([[ 0, 1, 2, 3],
 [ 4, 5, 6, 7],
 [ 8, 9, 10, 11]])
>>> a[2] ➎
array([ 8, 9, 10, 11])
>>> a[2, 1] ➏
9
>>> a[:, 1] ➐
array([1, 5, 9])
>>> a.transpose() ➑
array([[ 0, 4, 8],
 [ 1, 5, 9],
 [ 2, 6, 10],
 [ 3, 7, 11]])
➊ 安装 NumPy 之后，导入它（NumPy 并不是 Python 标准库的一部分）。
➋ 新建一个 0~11 的整数的 numpy.ndarry，然后把它打印出来。
➌ 看看数组的维度，它是一个一维的、有 12 个元素的数组。
➍ 把数组变成二维的，然后把它打印出来看看。
➎ 打印出第 2 行。
➏ 打印第 2 行第 1 列的元素。
➐ 把第 1 列打印出来。
➑ 把行和列交换，就得到了一个新数组。
```

```python
#NumPy 也可以对 numpy.ndarray 中的元素进行抽象的读取、保存和其他操作：
>>> import numpy
>>> floats = numpy.loadtxt('floats-10M-lines.txt') ➊
>>> floats[-3:] ➋
array([ 3016362.69195522, 535281.10514262, 4566560.44373946])
>>> floats *= .5 ➌
>>> floats[-3:]
array([ 1508181.34597761, 267640.55257131, 2283280.22186973])
>>> from time import perf_counter as pc ➍
>>> t0 = pc(); floats /= 3; pc() - t0 ➎
0.03690556302899495
>>> numpy.save('floats-10M', floats) ➏
>>> floats2 = numpy.load('floats-10M.npy', 'r+') ➐
>>> floats2 *= 6
>>> floats2[-3:] ➑
memmap([3016362.69195522, 535281.10514262, 4566560.44373946])
➊ 从文本文件里读取 1000 万个浮点数。
➋ 利用序列切片来读取其中的最后 3 个数。
➌ 把数组里的每个数都乘以 0.5，然后再看看最后 3 个数。
➍ 导入精度和性能都比较高的计时器（Python 3.3 及更新的版本中都有这个库）。
➎ 把每个元素都除以 3，可以看到处理 1000 万个浮点数所需的时间还不足 40 毫秒。
➏ 把数组存入后缀为 .npy 的二进制文件。
➐ 将上面的数据导入到另外一个数组里，这次 load 方法利用了一种叫作内存映射的机制，
它让我们在内存不足的情况下仍然可以对数组做切片。
➑ 把数组里每个数乘以 6 之后，再检视一下数组的最后 3 个数。
```

#### 2.9.4　双向队列和其他形式的队列

利用 .append 和 .pop 方法，我们可以把列表当作栈或者队列来用（比如，把 .append
和 .pop(0) 合起来用，就能模拟栈的“先进先出”的特点）

collections.deque 类（双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型。而且如果想要有一种数据类型来存放“最近用到的几个元素”，deque 也是一个很好的选择。这是因为在新建一个双向队列的时候，你可以指定这个队列的大小，如果这个队列满员了，还可以从反向端删除过期的元素，然后在尾端添加新的元素

```python
#示例 2-23 使用双向队列
>>> from collections import deque
>>> dq = deque(range(10), maxlen=10) ➊
>>> dq
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> dq.rotate(3) ➋
>>> dq
deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
>>> dq.rotate(-4)
>>> dq
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
>>> dq.appendleft(-1) ➌
>>> dq
deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> dq.extend([11, 22, 33]) ➍
>>> dq
deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
>>> dq.extendleft([10, 20, 30, 40]) ➎
>>> dq
deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
➊ maxlen 是一个可选参数，代表这个队列可以容纳的元素的数量，而且一旦设定，这个
属性就不能修改了。
➋ 队列的旋转操作接受一个参数 n，当 n > 0 时，队列的最右边的 n 个元素会被移动到队
列的左边。当 n < 0 时，最左边的 n 个元素会被移动到右边。
➌ 当试图对一个已满（len(d) == d.maxlen）的队列做尾部添加操作的时候，它头部的元
素会被删除掉。注意在下一行里，元素 0 被删除了。
➍ 在尾部添加 3 个元素的操作会挤掉 -1、1 和 2。
➎ extendleft(iter) 方法会把迭代器里的元素逐个添加到双向队列的左边，因此迭代器里
的元素会逆序出现在队列里。
```

## 第 3 章字典和集合

### 3.1　泛映射类型
