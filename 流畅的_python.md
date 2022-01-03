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

```python
#isinstance 一起被用来判定某个数据是不是广义上的映射类型
>>> my_dict = {}
>>> isinstance(my_dict, abc.Mapping)
True
```

这里用 isinstance 而不是 type 来检查某个参数是否为 dict 类型，因为这个参数有可能不
是 dict，而是一个比较另类的映射类型。

```python
>>> tt = (1, 2, (30, 40))
>>> hash(tt)
8027212646858338501
>>> tl = (1, 2, [30, 40])
>>> hash(tl)
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> tf = (1, 2, frozenset([30, 40]))
>>> hash(tf)
-4118419923444501110
```

元组本身是不可变序列，它里面的元素可能是其他可变类型的引用

```python
#创建字典的不同方式
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
>>> e = dict({'three': 3, 'one': 1, 'two': 2})
>>> a == b == c == d == e
True
```

### 3.2　字典推导

字典推导（dictcomp）可以从任何以键值对作为元素的可迭代对象中构建出字典。

```python
#示例 3-1　字典推导的应用
>>> DIAL_CODES = [ ➊
... (86, 'China'),
... (91, 'India'),
... (1, 'United States'),
... (62, 'Indonesia'),
... (55, 'Brazil'),
... (92, 'Pakistan'),
... (880, 'Bangladesh'),
... (234, 'Nigeria'),
... (7, 'Russia'),
... (81, 'Japan'),
... ]
>>> country_code = {country: code for code, country in DIAL_CODES} ➋
>>> country_code
{'China': 86, 'India': 91, 'Bangladesh': 880, 'United States': 1,
'Pakistan': 92, 'Japan': 81, 'Russia': 7, 'Brazil': 55, 'Nigeria':
234, 'Indonesia': 62}
>>> {code: country.upper() for country, code in country_code.items() ➌
... if code < 66}
{1: 'UNITED STATES', 55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA'}
➊ 一个承载成对数据的列表，它可以直接用在字典的构造方法中。
➋ 这里把配好对的数据左右换了下，国家名是键，区域码是值。
➌ 跟上面相反，用区域码作为键，国家名称转换为大写，并且过滤掉区域码大于或等于66 的地区。
```

### 3.3　常见的映射方法

用setdefault处理找不到的键

当字典 d[k] 不能找到正确的键的时候，Python 会抛出异常，这个行为符合 Python 所信奉的“快速失败”哲学。也许每个 Python 程序员都知道可以用 d.get(k, default) 来代替 d[k]，给找不到的键一个默认的返回值（这比处理 KeyError 要方便不少）。

```python
#示例 3-2 index0.py 这段程序从索引中获取单词出现的频率信息，并把它们写进对应的列表里（更好的解决方案在示例 3-4 中）
"""创建一个从单词到其出现情况的映射"""
import sys
import re
WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
 for line_no, line in enumerate(fp, 1):
 for match in WORD_RE.finditer(line):
 word = match.group()
 column_no = match.start()+1
 location = (line_no, column_no)
 # 这其实是一种很不好的实现，这样写只是为了证明论点
 occurrences = index.get(word, []) ➊
 occurrences.append(location) ➋
 index[word] = occurrences ➌
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper): ➍
 print(word, index[word])
➊ 提取 word 出现的情况，如果还没有它的记录，返回 []。
➋ 把单词新出现的位置添加到列表的后面。
➌ 把新的列表放回字典中，这又牵扯到一次查询操作。
➍ sorted 函数的 key= 参数没有调用 str.uppper，而是把这个方法的引用传递给 sorted 函
数，这样在排序的时候，单词会被规范成统一格式。2
```

```python
#示例 3-3 这里是示例 3-2 的不完全输出，每一行的列表都代表一个单词的出现情况，列表中的元素是一对值，第一个值表示出现的行，第二个表示出现的列
$ python3 index0.py ../../data/zen.txt
a [(19, 48), (20, 53)]
Although [(11, 1), (16, 1), (18, 1)]
ambiguity [(14, 16)]
and [(15, 23)]
are [(21, 12)]
aren [(10, 15)]
at [(16, 38)]
bad [(19, 50)]
be [(15, 14), (16, 27), (20, 50)]
beats [(11, 23)]
Beautiful [(3, 1)]
better [(3, 14), (4, 13), (5, 11), (6, 12), (7, 9), (8, 11),
(17, 8), (18, 25)]
...
```

```python
#示例 3-4 index.py 用一行就解决了获取和更新单词的出现情况列表，当然跟示例 3-2 不一样的是，这里用到了 dict.setdefault
"""创建从一个单词到其出现情况的映射"""
import sys
import re
WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
 for line_no, line in enumerate(fp, 1):
 for match in WORD_RE.finditer(line):
 word = match.group()
 column_no = match.start()+1
 location = (line_no, column_no)
 index.setdefault(word, []).append(location) ➊
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
 print(word, index[word])
➊ 获取单词的出现情况列表，如果单词不存在，把单词和一个空列表放进映射，然后返回
这个空列表，这样就能在不进行第二次查找的情况下更新列表了。
```

```python
也就是说，这样写：
my_dict.setdefault(key, []).append(new_value)
跟这样写：
if key not in my_dict:
 my_dict[key] = []
my_dict[key].append(new_value)
二者的效果是一样的，只不过后者至少要进行两次键查询——如果键不存在的话，就是三次，用 setdefault 只需要一次就可以完成整个操作。
```

### 3.4　映射的弹性键查询

#### 3.4.1 defaultdict：处理找不到的键的一个选择

比如，我们新建了这样一个字典：dd = defaultdict(list)，如果键 'new-key' 在 dd 中还
不存在的话，表达式 dd['new-key'] 会按照以下的步骤来行事。
(1) 调用 list() 来建立一个新列表。
(2) 把这个新列表作为值，'new-key' 作为它的键，放到 dd 中。
(3) 返回这个列表的引用。

```python
示例 3-5 index_default.py：利用 defaultdict 实例而不是 setdefault 方法
"""创建一个从单词到其出现情况的映射"""
import sys
import re
import collections
WORD_RE = re.compile(r'\w+')
index = collections.defaultdict(list) ➊
with open(sys.argv[1], encoding='utf-8') as fp:
 for line_no, line in enumerate(fp, 1):
 for match in WORD_RE.finditer(line):
 word = match.group()
 column_no = match.start()+1
 location = (line_no, column_no)
 index[word].append(location) ➋
# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
 print(word, index[word])
➊ 把 list 构造方法作为 default_factory 来创建一个 defaultdict。
➋ 如果 index 并没有 word 的记录，那么 default_factory 会被调用，为查询不到的键创造
一个值。这个值在这里是一个空的列表，然后这个空列表被赋值给 index[word]，继而
被当作返回值返回，因此 .append(location) 操作总能成功。
```

如果在创建 defaultdict 的时候没有指定 default_factory，查询不存在的键会触发KeyError。

所有这一切背后的功臣其实是特殊方法 __missing__。它会在 defaultdict 遇到找不到的键的时候调用 default_factory，而实际上这个特性是所有映射类型都可以选择去支持的。

#### 3.4.2　特殊方法__missing__

__missing__ 方法只会被 __getitem__ 调用（比如在表达式 d[k] 中）。提供
__missing__ 方法对 get 或者 __contains__（in 运算符会用到这个方法）

```python
示例 3-6 当有非字符串的键被查找的时候，StrKeyDict0 是如何在该键不存在的情况下，
把它转换为字符串的
Tests for item retrieval using `d[key]` notation::
 >>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
 >>> d['2']
 'two'
 >>> d[4]
 'four'
 >>> d[1]
 Traceback (most recent call last):
 ...
 KeyError: '1'
Tests for item retrieval using `d.get(key)` notation::
 >>> d.get('2')
 'two'
 >>> d.get(4)
 'four'
 >>> d.get(1, 'N/A')
 'N/A'
Tests for the `in` operator::
 >>> 2 in d
 True
 >>> 1 in d
 False
```

```python
示例 3-7 StrKeyDict0 在查询的时候把非字符串的键转换为字符串
class StrKeyDict0(dict): ➊
 def __missing__(self, key):
 if isinstance(key, str): ➋
 raise KeyError(key)
 return self[str(key)] ➌
 def get(self, key, default=None):
 try:
 return self[key] ➍
 except KeyError:
 return default ➎
 def __contains__(self, key):
 return key in self.keys() or str(key) in self.keys() ➏
➊ StrKeyDict0 继承了 dict。
➋ 如果找不到的键本身就是字符串，那就抛出 KeyError 异常。
➌ 如果找不到的键不是字符串，那么把它转换成字符串再进行查找。
➍ get 方法把查找工作用 self[key] 的形式委托给 __getitem__，这样在宣布查找失败之
前，还能通过 __missing__ 再给某个键一个机会。
➎ 如果抛出 KeyError，那么说明 __missing__ 也失败了，于是返回 default。
➏ 先按照传入键的原本的值来查找（我们的映射类型中可能含有非字符串的键），如果没
找到，再用 str() 方法把键转换成字符串再查找一次。
```

### 3.5　字典的变种

collections.OrderedDict :这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的。OrderedDict的 popitem 方法默认删除并返回的是字典里的最后一个元素，但是如果像 my_odict.popitem(last=False) 这样调用它，那么它删除并返回第一个被添加进去的元素。

collections.ChainMap
该类型可以容纳数个不同的映射对象，然后在进行键查找操作的时候，这些对象会被当作一个整体被逐个查找，直到键被找到为止。这个功能在给有嵌套作用域的语言做解释器的时候很有用，可以用一个映射对象来代表一个作用域的上下文。

collections.Counter
这个映射类型会给键准备一个整数计数器。每次更新一个键的时候都会增加这个计数器。所以这个类型可以用来给可散列表对象计数，或者是当成多重集来用——多重集合就是集合里的元素可以出现不止一次。Counter 实现了 + 和 - 运算符用来合并记录，还有像 most_common([n]) 这类很有用的方法。most_common([n]) 会按照次序返回映射里最常见的 n 个键和它们的计数

```python
>>> ct = collections.Counter('abracadabra')
>>> ct
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
>>> ct.update('aaaaazzz')
>>> ct
Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
>>> ct.most_common(2)
[('a', 10), ('z', 3)]
```

### 3.6　子类化UserDict

UserDict 并不是 dict 的子类，但是 UserDict 有一个叫作
data 的属性，是 dict 的实例，这个属性实际上是 UserDict 最终存储数据的地方

```python
#示例 3-8　无论是添加、更新还是查询操作，StrKeyDict 都会把非字符串的键转换为字符串
import collections
class StrKeyDict(collections.UserDict): ➊
 def __missing__(self, key): ➋
 if isinstance(key, str):
 raise KeyError(key)
 return self[str(key)]
 def __contains__(self, key):
 return str(key) in self.data ➌
 def __setitem__(self, key, item):
 self.data[str(key)] = item ➍
➊ StrKeyDict 是对 UserDict 的扩展。
➋ __missing__ 跟示例 3-7 里的一模一样。
➌ __contains__ 则更简洁些。这里可以放心假设所有已经存储的键都是字符串。因此，只
要在 self.data 上查询就好了，并不需要像 StrKeyDict0 那样去麻烦 self.keys()。
➍ __setitem__ 会把所有的键都转换成字符串。由于把具体的实现委托给了 self.data 属
性，这个方法写起来也不难
```

MutableMapping.update
这个方法不但可以为我们所直接利用，它还用在 __init__ 里，让构造方法可以利用传入的各种参数（其他映射类型、元素是 (key, value) 对的可迭代对象和键值参数）来新建实例。因为这个方法在背后是用 self[key] = value 来添加新值的，所以它其实是在使用我们的 __setitem__ 方法。

Mapping.get
在 StrKeyDict0（示例 3-7） 中， 我 们 不 得 不 改 写 get 方 法， 好 让 它 的 表 现 跟__getitem__ 一致。而在示例 3-8 中就没这个必要了，因为它继承了 Mapping.get 方法

### 3.7　不可变映射类型

```python
#示例 3-9　用 MappingProxyType 来获取字典的只读实例 mappingproxy
>>> from types import MappingProxyType
>>> d = {1:'A'}
>>> d_proxy = MappingProxyType(d)
>>> d_proxy
mappingproxy({1: 'A'})
>>> d_proxy[1] ➊
```

### 3.8　集合论

本书中“集”或者“集合”既指 set，也指 frozenset。当“集”仅指代 set类时，我会用等宽字体表示 7

```python
#集合的本质是许多唯一对象的聚集。因此，集合可以用于去重：
>>> l = ['spam', 'spam', 'eggs', 'spam']
>>> set(l)
{'eggs', 'spam'}
>>> list(set(l))
['eggs', 'spam']
```

集合还实现了很多基础的中缀运算符 。给定两个集合 a 和 b，a | b 返回的是它们的合集，a & b 得到的是交集，而 a - b 得到的是差集。

```python
#示例 3-10 needles 的元素在 haystack 里出现的次数，两个变量都是 set 类型
found = len(needles & haystack)
```

```python
#示例 3-11 needles 的元素在 haystack 里出现的次数（作用和示例 3-10 中的相同）
found = 0
for n in needles:
 if n in haystack:
 found += 1
```

```python
示例 3-12 needles 的元素在 haystack 里出现的次数，这次的代码可以用在任何可迭代对
象上
found = len(set(needles) & set(haystack))
# 另一种写法：
found = len(set(needles).intersection(haystack))
```

#### 3.8.1　集合字面量

```python
>>> s = {1}
>>> type(s)
<class 'set'>
>>> s
{1}
>>> s.pop()
1
>>> s
set()
```

```python
用 dis.dis（反汇编函数）来看看两个方法的字节码的不同：
>>> from dis import dis
>>> dis('{1}') ➊
 1 0 LOAD_CONST 0 (1)
 3 BUILD_SET 1 ➋
 6 RETURN_VALUE
>>> dis('set([1])') ➌
 1 0 LOAD_NAME 0 (set) ➍
 3 LOAD_CONST 0 (1)
 6 BUILD_LIST 1
 9 CALL_FUNCTION 1 (1 positional, 0 keyword pair)
 12 RETURN_VALUE
➊ 检查 {1} 字面量背后的字节码。
➋ 特殊的字节码 BUILD_SET 几乎完成了所有的工作。
➌ set([1]) 的字节码。
➍ 3 种不同的操作代替了上面的 BUILD_SET：LOAD_NAME、BUILD_LIST 和 CALL_FUNCTION。
```

```python
>>> frozenset(range(10))
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
```

#### 3.8.2　集合推导

```python
示例 3-13 新建一个 Latin-1 字符集合，该集合里的每个字符的 Unicode 名字里都有
“SIGN”这个单词
>>> from unicodedata import name ➊
>>> {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')} ➋
{'§', '=', '¢', '#', '¤', '<', '¥', 'μ', '×', '$', '¶', '£', '©',
'°', '+', '÷', '±', '>', '¬', '®', '%'}
➊ 从 unicodedata 模块里导入 name 函数，用以获取字符的名字。
➋ 把编码在 32~255 之间的字符的名字里有“SIGN”单词的挑出来，放到一个集合里。
```

#### 3.9 dict和set的背后

#### 3.9.1　一个关于效率的实验

```python
#示例 3-14 在 haystack 里查找 needles 的元素，并计算找到的元素的个数
found = 0
for n in needles:
 if n in haystack:
 found += 1
```

然后这段基准测试重复了 4 次，每次都把 haystack 的大小变成了上一次的 10 倍，直到里面有 1000 万个元素。

#### 3.9.2　字典中的散列表

散列表其实是一个稀疏数组（总是有空白元素的数组称为稀疏数组）。在一般的数据结构教材中，散列表里的单元通常叫作表元（bucket）。在 dict 的散列表当中，每个键值对都占用一个表元，每个表元都有两个部分，一个是对键的引用，另一个是对值的引用。因为所有表元的大小一致，所以可以通过偏移量来读取某个表元。

#### 3.9.3 dict的实现及其导致的结果

1. 键必须是可散列的

一个可散列的对象必须满足以下要求。
(1) 支持 hash() 函数，并且通过 __hash__() 方法所得到的散列值是不变的。
(2) 支持通过 __eq__() 方法来检测相等性。
(3) 若 a == b 为真，则 hash(a) == hash(b) 也为真。

所有由用户自定义的对象默认都是可散列的，因为它们的散列值由 id() 来获取，而且它们都是不相等的。

如果你实现了一个类的 __eq__ 方法，并且希望它是可散列的，那么它一定要有个恰当的 __hash__ 方法，保证在 a == b 为真的情况下 hash(a) == hash(b)也必定为真。否则就会破坏恒定的散列表算法，导致由这些对象所组成的字典和集合完全失去可靠性，这个后果是非常可怕的。另一方面，如果一个
含有自定义的 __eq__ 依赖的类处于可变的状态，那就不要在这个类中实现__hash__ 方法，因为它的实例是不可散列的。

```python
示例 3-17 dialcodes.py 将同样的数据以不同的顺序添加到 3 个字典里
# 世界人口数量前10位国家的电话区号
DIAL_CODES = [
 (86, 'China'),
 (91, 'India'),
 (1, 'United States'),
 (62, 'Indonesia'),
 (55, 'Brazil'),
 (92, 'Pakistan'),
 (880, 'Bangladesh'),
 (234, 'Nigeria'),
 (7, 'Russia'),
 (81, 'Japan'),
 ]
d1 = dict(DIAL_CODES) ➊
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES)) ➋
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1])) ➌
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3 ➍
➊ 创建 d1 的时候，数据元组的顺序是按照国家的人口排名来决定的。
➋ 创建 d2 的时候，数据元组的顺序是按照国家的电话区号来决定的。
➌ 创建 d3 的时候，数据元组的顺序是按照国家名字的英文拼写来决定的。
➍ 这些字典是相等的，因为它们所包含的数据是一样的。
```

```python
#示例 3-18 里是上面例子的输出。
#示例 3-18 dialcodes.py 的输出中，3 个字典的键的顺序是不一样的
d1: dict_keys([880, 1, 86, 55, 7, 234, 91, 92, 62, 81])
d2: dict_keys([880, 1, 91, 86, 81, 55, 234, 7, 92, 62])
d3: dict_keys([880, 81, 1, 86, 55, 7, 234, 91, 92, 62])
```

## 第 4 章 文本和字节序列

### 4.1　字符问题

```python
示例 4-1　编码和解码
>>> s = 'café'
>>> len(s) # ➊
4
>>> b = s.encode('utf8') # ➋
>>> b
b'caf\xc3\xa9' # ➌
>>> len(b) # ➍
5
>>> b.decode('utf8') # ➎
'café'
➊ 'café' 字符串有 4 个 Unicode 字符。
➋ 使用 UTF-8 把 str 对象编码成 bytes 对象。
➌ bytes 字面量以 b 开头。
➍ 字节序列 b 有 5 个字节（在 UTF-8 中，“é”的码位编码成两个字节）。
➎ 使用 UTF-8 把 bytes 对象解码成 str 对象。
```

### 4.2　字节概要

```python
#示例 4-2　包含 5 个字节的 bytes 和 bytearray 对象
>>> cafe = bytes('café', encoding='utf_8') ➊
>>> cafe
b'caf\xc3\xa9'
>>> cafe[0] ➋
99
>>> cafe[:1] ➌
b'c'
>>> cafe_arr = bytearray(cafe)
>>> cafe_arr ➍
bytearray(b'caf\xc3\xa9')
>>> cafe_arr[-1:] ➎
bytearray(b'\xa9')
➊ bytes 对象可以从 str 对象使用给定的编码构建。
➋ 各个元素是 range(256) 内的整数。
➌ bytes 对象的切片还是 bytes 对象，即使是只有一个字节的切片。
➍ bytearray 对象没有字面量句法，而是以 bytearray() 和字节序列字面量参数的形式显示。
➎ bytearray 对象的切片还是 bytearray 对象。
```

```python
示例 4-3　使用数组中的原始数据初始化 bytes 对象
>>> import array
>>> numbers = array.array('h', [-2, -1, 0, 1, 2]) ➊
>>> octets = bytes(numbers) ➋
>>> octets
b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00' ➌
➊ 指定类型代码 h，创建一个短整数（16 位）数组。
➋ octets 保存组成 numbers 的字节序列的副本。
➌ 这些是表示那 5 个短整数的 10 个字节。
```

结构体和内存视图

```python
示例 4-4　使用 memoryview 和 struct 查看一个 GIF 图像的首部
>>> import struct
>>> fmt = '<3s3sHH' # ➊
>>> with open('filter.gif', 'rb') as fp:
... img = memoryview(fp.read()) # ➋
...
>>> header = img[:10] # ➌
>>> bytes(header) # ➍
b'GIF89a+\x02\xe6\x00'
>>> struct.unpack(fmt, header) # ➎
(b'GIF', b'89a', 555, 230)
>>> del header # ➏
>>> del img
➊ 结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数。
➋ 使用内存中的文件内容创建一个 memoryview 对象……
➌ ……然后使用它的切片再创建一个 memoryview 对象；这里不会复制字节序列。
➍ 转换成字节序列，这只是为了显示；这里复制了 10 字节。
➎ 拆包 memoryview 对象，得到一个元组，包含类型、版本、宽度和高度。
➏ 删除引用，释放 memoryview 实例所占的内存。
```

### 4.3　基本的编解码器

```python
示例 4-5　使用 3 个编解码器编码字符串“El Niño”，得到的字节序列差异很大
>>> for codec in ['latin_1', 'utf_8', 'utf_16']:
... print(codec, 'El Niño'.encode(codec), sep='\t')
...
latin_1 b'El Ni\xf1o'
utf_8 b'El Ni\xc3\xb1o'
utf_16 b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
```

latin1（即 iso8859_1）
一种重要的编码，是其他编码的基础，例如 cp1252 和 Unicode（注意，latin1 与
cp1252 的字节值是一样的，甚至连码位也相同）。

utf-8
目前 Web 中最常见的 8 位编码；3 与 ASCII 兼容（纯 ASCII 文本是有效的 UTF-8 文本）。

utf-16le
UTF-16 的 16 位编码方案的一种形式；所有 UTF-16 支持通过转义序列（称为“代理对”，surrogate pair）表示超过 U+FFFF 的码位。

### 4.4　了解编解码问题

#### 4.4.1　处理UnicodeEncodeError

```python
示例 4-6　编码成字节序列：成功和错误处理
>>> city = 'São Paulo'
>>> city.encode('utf_8') ➊
b'S\xc3\xa3o Paulo'
>>> city.encode('utf_16')
b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
>>> city.encode('iso8859_1') ➋
b'S\xe3o Paulo'
>>> city.encode('cp437') ➌
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
 return codecs.charmap_encode(input,errors,encoding_map)
UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
position 1: character maps to <undefined>
>>> city.encode('cp437', errors='ignore') ➍
b'So Paulo'
>>> city.encode('cp437', errors='replace') ➎
b'S?o Paulo'
>>> city.encode('cp437', errors='xmlcharrefreplace') ➏
b'S&#227;o Paulo'
➊ 'utf_?' 编码能处理任何字符串。
➋ 'iso8859_1' 编码也能处理字符串 'São Paulo'。
➌ 'cp437' 无法编码 'ã'（带波形符的“a”）。默认的错误处理方式 'strict' 抛出 UnicodeEncodeError。
➍ error='ignore' 处理方式悄无声息地跳过无法编码的字符；这样做通常很是不妥。
➎ 编码时指定 error='replace'，把无法编码的字符替换成 '?'；数据损坏了，但是用户知
道出了问题。
➏ 'xmlcharrefreplace' 把无法编码的字符替换成 XML 实体。
```

#### 4.4.2　处理UnicodeDecodeError

```python
示例 4-7　把字节序列解码成字符串：成功和错误处理
>>> octets = b'Montr\xe9al' ➊
>>> octets.decode('cp1252') ➋
'Montréal'
>>> octets.decode('iso8859_7') ➌
'Montrιal'
>>> octets.decode('koi8_r') ➍
'MontrИal'
>>> octets.decode('utf_8') ➎
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:
invalid continuation byte
>>> octets.decode('utf_8', errors='replace') ➏
'Montr�al'
➊ 这些字节序列是使用 latin1 编码的“Montréal”；'\xe9' 字节对应“é”。
➋ 可以使用 'cp1252'（Windows 1252）解码，因为它是 latin1 的有效超集。
➌ ISO-8859-7 用于编码希腊文，因此无法正确解释 '\xe9' 字节，而且没有抛出错误。
➍ KOI8-R 用于编码俄文；这里，'\xe9' 表示西里尔字母“И”。
➎ 'utf_8' 编解码器检测到 octets 不是有效的 UTF-8 字符串，抛出 UnicodeDecodeError。
➏ 使用 'replace' 错误处理方式，\xe9 替换成了“�”（码位是 U+FFFD），这是官方指定
的 REPLACEMENT CHARACTER（替换字符），表示未知字符。
```

#### 4.4.3　使用预期之外的编码加载模块时抛出的SyntaxError

```python
示例 4-8 ola.py：“你好，世界！”的葡萄牙语版
# coding: cp1252
print('Olá, Mundo!')
```

#### 4.4.4　如何找出字节序列的编码

#### 4.4.5 BOM：有用的鬼符

```python
>>> u16 = 'El Niño'.encode('utf_16')
>>> u16
b'\xff\xfeE\x00l\x00 \x00N\x00i\x00\xf1\x00o\x00'
```

我指的是 b'\xff\xfe'。这是 BOM，即字节序标记（byte-order mark），指明编码时使用Intel CPU 的小字节序

UTF-16 有两个变种：UTF-16LE，显式指明使用小字节序； UTF-16BE，显式指明使用大字节序。

如果使用这两个变种，不会生成 BOM：

```python
>>> u16le = 'El Niño'.encode('utf_16le')
>>> list(u16le)
[69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111, 0]
>>> u16be = 'El Niño'.encode('utf_16be')
>>> list(u16be)
[0, 69, 0, 108, 0, 32, 0, 78, 0, 105, 0, 241, 0, 111]
```

UTF-8 的一大优势是，不管设备使用哪种字节序，生成的字节序列始终一致，因此不需要 BOM

### 4.5　处理文本文件

```python
#示例 4-9　一个平台上的编码问题（如果在你的机器上运行，它可能会发生，也可能不会）
>>> open('cafe.txt', 'w', encoding='utf_8').write('café')
4
>>> open('cafe.txt').read()
'cafÃ©'
```

问题是：写入文件时指定了 UTF-8 编码，但是读取文件时没有这么做，因此 Python 假定要使用系统默认的编码（Windows 1252），于是文件的最后一个字节解码成了字符 'Ã©'，而不是 'é'。

```python
示例 4-10 仔细分析在 Windows 中运行的示例 4-9，找出并修正问题
>>> fp = open('cafe.txt', 'w', encoding='utf_8')
>>> fp ➊
<_io.TextIOWrapper name='cafe.txt' mode='w' encoding='utf_8'>
>>> fp.write('café')
4 ➋
>>> fp.close()
>>> import os
>>> os.stat('cafe.txt').st_size
5 ➌
>>> fp2 = open('cafe.txt')
>>> fp2 ➍
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='cp1252'>
>>> fp2.encoding ➎
'cp1252'
>>> fp2.read() 
'cafÃ©' ➏
>>> fp3 = open('cafe.txt', encoding='utf_8') ➐
>>> fp3
<_io.TextIOWrapper name='cafe.txt' mode='r' encoding='utf_8'>
>>> fp3.read()
'café' ➑
>>> fp4 = open('cafe.txt', 'rb') ➒
>>> fp4
<_io.BufferedReader name='cafe.txt'> ➓
>>> fp4.read()  # 读取返回的字节序列，结果与预期相符。
b'caf\xc3\xa9'
➊ 默认情况下，open 函数采用文本模式，返回一个 TextIOWrapper 对象。
➋ 在 TextIOWrapper 对象上调用 write 方法返回写入的 Unicode 字符数。
➌ os.stat 报告文件中有 5 个字节；UTF-8 编码的 'é' 占两个字节，0xc3 和 0xa9。
➍ 打开文本文件时没有显式指定编码，返回一个 TextIOWrapper 对象，编码是区域设置中
的默认值。
➎ TextIOWrapper 对象有个 encoding 属性；查看它，发现这里的编码是 cp1252。
➏ 在 Windows cp1252 编码中，0xc3 字节是“Ã”（带波形符的 A），0xa9 字节是版权符号。
➐ 使用正确的编码打开那个文件。
➑ 结果符合预期：得到的是四个 Unicode 字符 'café'。
➒ 'rb' 标志指明在二进制模式中读取文件。
➓ 返回的是 BufferedReader 对象，而不是 TextIOWrapper 对象。
```

```python
示例 4-11 探索编码默认值
import sys, locale
expressions = """
 locale.getpreferredencoding()
 type(my_file)
 my_file.encoding
 sys.stdout.isatty()
 sys.stdout.encoding
 sys.stdin.isatty() 
 sys.stdin.encoding
 sys.stderr.isatty()
 sys.stderr.encoding
 sys.getdefaultencoding()
 sys.getfilesystemencoding()
 """
my_file = open('dummy', 'w')
for expression in expressions.split():
 value = eval(expression)
 print(expression.rjust(30), '->', repr(value))
```

```python
$ python3 default_encodings.py
 locale.getpreferredencoding() -> 'UTF-8'
 type(my_file) -> <class '_io.TextIOWrapper'>
 my_file.encoding -> 'UTF-8'
 sys.stdout.isatty() -> True
 sys.stdout.encoding -> 'UTF-8'
 sys.stdin.isatty() -> True
 sys.stdin.encoding -> 'UTF-8'
 sys.stderr.isatty() -> True
 sys.stderr.encoding -> 'UTF-8'
 sys.getdefaultencoding() -> 'utf-8'
 sys.getfilesystemencoding() -> 'utf-8'
```

```python
示例 4-12 在 Windows 7（SP1）巴西版中的 cmd.exe 中输出的默认编码；PowerShell 输
出的结果相同
Z:\>chcp ➊
Página de código ativa: 850
Z:\>python default_encodings.py ➋
 locale.getpreferredencoding() -> 'cp1252' ➌
 type(my_file) -> <class '_io.TextIOWrapper'>
 my_file.encoding -> 'cp1252' ➍
 sys.stdout.isatty() -> True ➎
 sys.stdout.encoding -> 'cp850' ➏
 sys.stdin.isatty() -> True
 sys.stdin.encoding -> 'cp850'
 sys.stderr.isatty() -> True
 sys.stderr.encoding -> 'cp850'
 sys.getdefaultencoding() -> 'utf-8'
 sys.getfilesystemencoding() -> 'mbcs'
➊ chcp 输出当前控制台激活的代码页：850。
➋ 运行 default_encodings.py，把结果输出到控制台。
➌ locale.getpreferredencoding() 是最重要的设置。
➍ 文本文件默认使用 locale.getpreferredencoding()。
```

### 4.6　为了正确比较而规范化Unicode字符串

```python
“café”这个词可以使用两种方式构成，分别有 4 个和 5 个码位，但是结果完全一样：
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1, s2
('café', 'café')
>>> len(s1), len(s2)
(4, 5)
>>> s1 == s2
False
```

U+0301 是 COMBINING ACUTE ACCENT，加在“e”后面得到“é”'é' 和'e\u0301' 这样的序列叫“标准等价物”（canonical equivalent），应用程序应该把它们视作相同的字符。但是，Python 看到的是不同的码位序列，因此判定二者不相等

这个问题的解决方案是使用 unicodedata.normalize 函数提供的 Unicode 规范化

```python
#NFC（Normalization Form C）使用最少的码位构成等价的字符串，而 NFD 把组合字符分解成基字符和单独的组合字符
>>> from unicodedata import normalize
>>> s1 = 'café' # 把"e"和重音符组合在一起
>>> s2 = 'cafe\u0301' # 分解成"e"和重音符
>>> len(s1), len(s2)
(4, 5)
>>> len(normalize('NFC', s1)), len(normalize('NFC', s2))
(4, 4)
>>> len(normalize('NFD', s1)), len(normalize('NFD', s2))
(5, 5) 
>>> from unicodedata import normalize
>>> s1 = 'café' # 把"e"和重音符组合在一起
>>> s2 = 'cafe\u0301' # 分解成"e"和重音符
>>> len(s1), len(s2)
(4, 5)
>>> len(normalize('NFC', s1)), len(normalize('NFC', s2))
(4, 4)
>>> len(normalize('NFD', s1)), len(normalize('NFD', s2))
(5, 5) 
>>> normalize('NFC', s1) == normalize('NFC', s2)
True
>>> normalize('NFD', s1) == normalize('NFD', s2)
True
```

西方键盘通常能输出组合字符，因此用户输入的文本默认是 NFC 形式。不过，安全起见，保存文本之前，最好使用 normalize('NFC', user_text) 清洗字符串。

```python
>>> from unicodedata import normalize, name
>>> ohm = '\u2126'
>>> name(ohm)
'OHM SIGN'
>>> ohm_c = normalize('NFC', ohm)
>>> name(ohm_c)
'GREEK CAPITAL LETTER OMEGA'
>>> ohm == ohm_c
False
>>> normalize('NFC', ohm) == normalize('NFC', ohm_c)
True
```

```python
>>> from unicodedata import normalize, name
>>> half = '½'
>>> normalize('NFKC', half)
'1⁄2'
>>> four_squared = '4²'
>>> normalize('NFKC', four_squared)
'42'
>>> micro = 'µ'
>>> micro_kc = normalize('NFKC', micro)
>>> micro, micro_kc
('µ', 'μ')
>>> ord(micro), ord(micro_kc)
(181, 956)
>>> name(micro), name(micro_kc)
('MICRO SIGN', 'GREEK SMALL LETTER MU')

```

#### 4.6.1　大小写折叠

大小写折叠其实就是把所有文本变成小写，再做些其他转换。这个功能由 str.casefold()方法（Python 3.3 新增）支持

```python
>>> micro = 'µ'
>>> name(micro)
'MICRO SIGN'
>>> micro_cf = micro.casefold()
>>> name(micro_cf)
'GREEK SMALL LETTER MU'
>>> micro, micro_cf
('µ', 'μ')
>>> eszett = 'ß'
>>> name(eszett)
'LATIN SMALL LETTER SHARP S'
>>> eszett_cf = eszett.casefold()
>>> eszett, eszett_cf
('ß', 'ss')
```

#### 4.6.2　规范化文本匹配实用函数

```python
示例 4-13 normeq.py：比较规范化 Unicode 字符串
"""
Utility functions for normalized Unicode string comparison.
Using Normal Form C, case sensitive:
 >>> s1 = 'café'
 >>> s2 = 'cafe\u0301'
 >>> s1 == s2
 False
 >>> nfc_equal(s1, s2)
 True
 >>> nfc_equal('A', 'a')
 False
Using Normal Form C with case folding:
 >>> s3 = 'Straße'
 >>> s4 = 'strasse'
 >>> s3 == s4
 False
 >>> nfc_equal(s3, s4)
 False
 >>> fold_equal(s3, s4)
 True
 >>> fold_equal(s1, s2)
 True
 >>> fold_equal('A', 'a')
 True
"""
from unicodedata import normalize
def nfc_equal(str1, str2):
 return normalize('NFC', str1) == normalize('NFC', str2)
def fold_equal(str1, str2):
 return (normalize('NFC', str1).casefold() ==
 normalize('NFC', str2).casefold())
```

## 第 5 章 一等函数

### 5.1 把函数视作对象

```python
#示例 5-1　创建并测试一个函数，然后读取它的 __doc__ 属性，再检查它的类型
>>> def factorial(n): ➊
... '''returns n!'''
... return 1 if n < 2 else n * factorial(n-1)
...
>>> factorial(42)
1405006117752879898543142606244511569936384000000000
>>> factorial.__doc__ ➋
'returns n!'
>>> type(factorial) ➌
<class 'function'>
➊ 这是一个控制台会话，因此我们是在“运行时”创建一个函数。
➋ __doc__ 是函数对象众多属性中的一个。
➌ factorial 是 function 类的实例。
```

### 示例 5-2　通过别的名称使用函数，再把函数作为参数传递

```python
>>> fact = factorial
>>> fact
<function factorial at 0x...>
>>> fact(5) #5的阶乘等于5乘4乘3乘2乘1=120
120
>>> map(factorial, range(11))
<map object at 0x...>
>>> list(map(fact, range(11)))
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
```

### 5.2　高阶函数

```python
#函数 sorted ：可选的 key 参数用于提供一个函数，它会应用到各个元素上进行排序
#示例 5-3　根据单词长度给一个列表排序
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=len)
['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
>>>
```

```python
#示例 5-4　根据反向拼写给一个单词列表排序
>>> def reverse(word):
... return word[::-1]
>>> reverse('testing')
'gnitset'
>>> sorted(fruits, key=reverse)
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
>>>
```

```python
示例 5-5　计算阶乘列表：map 和 filter 与列表推导比较
>>> list(map(fact, range(6))) ➊
[1, 1, 2, 6, 24, 120]
>>> [fact(n) for n in range(6)] ➋
[1, 1, 2, 6, 24, 120]
>>> list(map(factorial, filter(lambda n: n % 2, range(6)))) ➌
[1, 6, 120]
>>> [factorial(n) for n in range(6) if n % 2] ➍
[1, 6, 120]
>>>
➊ 构建 0! 到 5! 的一个阶乘列表。
➋ 使用列表推导执行相同的操作。
➌ 使用 map 和 filter 计算直到 5! 的奇数阶乘列表。
➍ 使用列表推导做相同的工作，换掉 map 和 filter，并避免了使用 lambda 表达式。
```

```python
#示例 5-6　使用 reduce 和 sum 计算 0~99 之和
>>> from functools import reduce ➊
>>> from operator import add ➋
>>> reduce(add, range(100)) ➌
4950
>>> sum(range(100)) ➍
4950
>>>
➊ 从 Python 3.0 起，reduce 不再是内置函数了。
➋ 导入 add，以免创建一个专求两数之和的函数。
➌ 计算 0~99 之和。
➍ 使用 sum 做相同的求和；无需导入或创建求和函数。
```

### 5.3　匿名函数

lambda 关键字在 Python 表达式内创建匿名函数。

```python
#示例 5-7　使用 lambda 表达式反转拼写，然后依此给单词列表排序
>>> fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
>>> sorted(fruits, key=lambda word: word[::-1])
['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']
>>>
```

### 5.4　可调用对象

用户定义的函数:使用 def 语句或 lambda 表达式创建。

内置函数:使用 C 语言（CPython）实现的函数，如 len 或 time.strftime。

内置方法:使用 C 语言实现的方法，如 dict.get。

方法:在类的定义体中定义的函数。

### 5.5　用户定义的可调用类型

```python
#示例 5-8 bingocall.py：调用 BingoCage 实例，从打乱的列表中取出一个元素
import random
class BingoCage:
    def __init__(self, items):
 self._items = list(items) ➊
 random.shuffle(self._items) ➋
 def pick(self): ➌
 try:
 return self._items.pop()
 except IndexError:
 raise LookupError('pick from empty BingoCage') ➍
 def __call__(self): ➎
 return self.pick()
➊ __init__ 接受任何可迭代对象；在本地构建一个副本，防止列表参数的意外副作用。
➋ shuffle 定能完成工作，因为 self._items 是列表。
➌ 起主要作用的方法。
➍ 如果 self._items 为空，抛出异常，并设定错误消息。
➎ bingo.pick() 的快捷方式是 bingo()。
```

```python
#下面是示例 5-8 中定义的类的简单演示。注意，bingo 实例可以作为函数调用，而且内置的 callable(...) 函数判定它是可调用的对象：
>>> bingo = BingoCage(range(3))
>>> bingo.pick()
1
>>> bingo()
0
>>> callable(bingo)
True
```

### 5.6　函数内省

```python
#使用 dir 函数可以探知 factorial 具有下述属性
>>> dir(factorial)
['__annotations__', '__call__', '__class__', '__closure__', '__code__',
'__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
'__gt__', '__hash__', '__init__', '__kwdefaults__', '__le__', '__lt__',
'__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__',
'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__']
>>>
```

```python
示例 5-9　列出常规对象没有而函数有的属性
>>> class C: pass # ➊
>>> obj = C() # ➋
>>> def func(): pass # ➌
>>> sorted(set(dir(func)) - set(dir(obj))) # ➍
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__',
'__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
>>>
➊ 创建一个空的用户定义的类。
➋ 创建一个实例。
➌ 创建一个空函数。
➍ 计算差集，然后排序，得到类的实例没有而函数有的属性列表。
```

### 5.7　从定位参数到仅限关键字参数

```python
#示例 5-10 tag 函数用于生成 HTML 标签；使用名为 cls 的关键字参数传入“class”属性，这是一种变通方法，因为“class”是 Python 的关键字
def tag(name, *content, cls=None, **attrs):
 """生成一个或多个HTML标签"""
 if cls is not None:
    attrs['class'] = cls
 if attrs:
    attr_str = ''.join(' %s="%s"' % (attr, value)
 for attr, value
    in sorted(attrs.items()))
 else:
    attr_str = ''
 if content:
 return '\n'.join('<%s%s>%s</%s>' %
 (name, attr_str, c, name) for c in content)
 else:
 return '<%s%s />' % (name, attr_str)
```

### 5.8　获取关于参数的信息

```python
示例 5-12 Bobo 知道 hello 需要 person 参数，并且从 HTTP 请求中获取它
import bobo

@bobo.query('/')
def hello(person):
 return 'Hello %s!' % person
```

```python
#示例 5-13 如果请求中缺少函数的参数，Bobo 返回 403 forbidden 响应；curl -i 的作用是把首部转储到标准输出
$ curl -i http://localhost:8080/
HTTP/1.0 403 Forbidden
Date: Thu, 21 Aug 2014 21:39:44 GMT
Server: WSGIServer/0.2 CPython/3.4.1
Content-Type: text/html; charset=UTF-8
Content-Length: 103
<html>
<head><title>Missing parameter</title></head>
<body>Missing form variable person</body>
</html>
```

```python
#示例 5-14 传入所需的 person 参数才能得到 OK 响应
$ curl -i http://localhost:8080/?person=Jim
HTTP/1.0 200 OK
Date: Thu, 21 Aug 2014 21:42:32 GMT
Server: WSGIServer/0.2 CPython/3.4.1
Content-Type: text/html; charset=UTF-8
Content-Length: 10
Hello Jim!
```

```python
#示例 5-15 在指定长度附近截断字符串的函数
def clip(text, max_len=80):
 """在max_len前面或后面的第一个空格处截断文本
 """
 end = None
 if len(text) > max_len:
    space_before = text.rfind(' ', 0, max_len)
 if space_before >= 0:
    end = space_before
 else: 
     space_after = text.rfind(' ', max_len)
 if space_after >= 0:
    end = space_after
 if end is None: # 没找到空格
    end = len(text)
 return text[:end].rstrip()
```

```python
#示例 5-16 提取关于函数参数的信息
>>> from clip import clip
>>> clip.__defaults__
(80,)
>>> clip.__code__ # doctest: +ELLIPSIS
<code object clip at 0x...>
>>> clip.__code__.co_varnames
('text', 'max_len', 'end', 'space_before', 'space_after')
>>> clip.__code__.co_argcount
2
```

```python
#示例 5-17 提取函数的签名 2
>>> from clip import clip
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig # doctest: +ELLIPSIS
<inspect.Signature object at 0x...>
>>> str(sig)
'(text, max_len=80)'
>>> for name, param in sig.parameters.items():
... print(param.kind, ':', name, '=', param.default)
...
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80
```

```python
kind 属性的值是 _ParameterKind 类中的 5 个值之一，列举如下。
POSITIONAL_OR_KEYWORD
可以通过定位参数和关键字参数传入的形参（多数 Python 函数的参数属于此类）。
VAR_POSITIONAL
定位参数元组。
VAR_KEYWORD
关键字参数字典。
KEYWORD_ONLY
仅限关键字参数（Python 3 新增）。
POSITIONAL_ONLY
仅限定位参数；目前，Python 声明函数的句法不支持，但是有些使用 C 语言实现且不接受关键字参数的函数（如 divmod）支持。
```

```python
#示例 5-18 把 tag 函数（见示例 5-10）的签名绑定到一个参数字典上 3
>>> import inspect
>>> sig = inspect.signature(tag) ➊
>>> my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
... 'src': 'sunset.jpg', 'cls': 'framed'}
>>> bound_args = sig.bind(**my_tag) ➋
>>> bound_args
<inspect.BoundArguments object at 0x...> ➌
>>> for name, value in bound_args.arguments.items(): ➍
... print(name, '=', value)
...
name = img
cls = framed
attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
>>> del my_tag['name'] ➎
>>> bound_args = sig.bind(**my_tag) ➏
Traceback (most recent call last):
 ...
TypeError: 'name' parameter lacking default value
➊ 获取 tag 函数（见示例 5-10）的签名。
➋ 把一个字典参数传给 .bind() 方法。
➌ 得到一个 inspect.BoundArguments 对象。
➍ 迭代 bound_args.arguments（一个 OrderedDict 对象）中的元素，显示参数的名称和值。
➎ 把必须指定的参数 name 从 my_tag 中删除。
➏ 调用 sig.bind(**my_tag)，抛出 TypeError，抱怨缺少 name 参数。
```

### 5.9　函数注解

```python
#示例 5-19 有注解的 clip 函数
def clip(text:str, max_len:'int > 0'=80) -> str: ➊
 """在max_len前面或后面的第一个空格处截断文本
 """
end = None
if len(text) > max_len:
    space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
if end is None: # 没找到空格
    end = len(text)
return text[:end].rstrip()
➊ 有注解的函数声明。
```

```python
#示例 5-20 从函数签名中提取注解
>>> from clip_annot import clip
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig.return_annotation
<class 'str'>
>>> for param in sig.parameters.values():
... note = repr(param.annotation).ljust(13)
... print(note, ':', param.name, '=', param.default)
<class 'str'> : text = <class 'inspect._empty'>
'int > 0' : max_len = 80
```

### 5.10　支持函数式编程的包

#### 5.10.1 operator模块

```python
#示例 5-21 使用 reduce 函数和一个匿名函数计算阶乘
from functools import reduce
def fact(n):
 return reduce(lambda a, b: a*b, range(1, n+1))
```

```python
#示例 5-22 使用 reduce 和 operator.mul 函数计算阶乘
from functools import reduce
from operator import mul
def fact(n):
 return reduce(mul, range(1, n+1))
```

```python
#示例 5-23 演示使用 itemgetter 排序一个元组列表（数据来自示例 2-8）
>>> metro_data = [
... ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
... ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
... ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
... ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
... ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
>>>
>>> from operator import itemgetter
>>> for city in sorted(metro_data, key=itemgetter(1)):
... print(city)
...
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('New York-Newark', 'US', 20.104, (40.808611, -74.020386))
```

```python
如果把多个参数传给 itemgetter，它构建的函数会返回提取的值构成的元组：
>>> cc_name = itemgetter(1, 0)
>>> for city in metro_data:
... print(cc_name(city))
...
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'Sao Paulo')
>>>
```

```python
#示例 5-24 定义一个 namedtuple，名为 metro_data（与示例 5-23 中的列表相同），演示使用 attrgetter 处理它
>>> from collections import namedtuple
>>> LatLong = namedtuple('LatLong', 'lat long') # ➊
>>> Metropolis = namedtuple('Metropolis', 'name cc pop coord') # ➋
>>> metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) # ➌
... for name, cc, pop, (lat, long) in metro_data]
>>> metro_areas[0]
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,
long=139.691667))
>>> metro_areas[0].coord.lat # ➍
35.689722
>>> from operator import attrgetter
>>> name_lat = attrgetter('name', 'coord.lat') # ➎
>>>
>>> for city in sorted(metro_areas, key=attrgetter('coord.lat')): # ➏
... print(name_lat(city)) # ➐
...
('Sao Paulo', -23.547778)
('Mexico City', 19.433333)
('Delhi NCR', 28.613889)
('Tokyo', 35.689722)
('New York-Newark', 40.808611)
➊ 使用 namedtuple 定义 LatLong。
➋ 再定义 Metropolis。
➌ 使用 Metropolis 实例构建 metro_areas 列表；注意，我们使用嵌套的元组拆包提取
(lat, long)，然后使用它们构建 LatLong，作为 Metropolis 的 coord 属性。
➍ 深入 metro_areas[0]，获取它的纬度。
➎ 定义一个 attrgetter，获取 name 属性和嵌套的 coord.lat 属性。
➏ 再次使用 attrgetter，按照纬度排序城市列表。
➐ 使用标号➎中定义的 attrgetter，只显示城市名和纬度。
```

```python
#下面是 operator 模块中定义的部分函数（省略了以 _ 开头的名称，因为它们基本上是实现细节）：4
>>> [name for name in dir(operator) if not name.startswith('_')]
['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains',
'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt',
'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imod', 'imul',
'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift',
'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le',
'length_hint', 'lshift', 'lt', 'methodcaller', 'mod', 'mul', 'ne',
'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub',
'truediv', 'truth', 'xor']
```

```python
#示例 5-25 methodcaller 使用示例：第二个测试展示绑定额外参数的方式
>>> from operator import methodcaller
>>> s = 'The time has come'
>>> upcase = methodcaller('upper')
>>> upcase(s)
'THE TIME HAS COME'
>>> hiphenate = methodcaller('replace', ' ', '-')
>>> hiphenate(s)
'The-time-has-come'
```

```python
#如果想把 str.upper 作为函数使用，只需在 str 类上调用，并传入一个字符串参数，如下所示：
>>> str.upper(s)
'THE TIME HAS COME'
```

#### 5.10.2　使用functools.partial冻结参数

```python
#示例 5-26 使用 partial 把一个两参数函数改编成需要单参数的可调用对象
>>> from operator import mul
>>> from functools import partial
>>> triple = partial(mul, 3) ➊
>>> triple(7) ➋
21
>>> list(map(triple, range(1, 10))) ➌
[3, 6, 9, 12, 15, 18, 21, 24, 27]
➊ 使用 mul 创建 triple 函数，把第一个定位参数定为 3。
➋ 测试 triple 函数。
➌ 在 map 中使用 triple；在这个示例中不能使用 mul。
```

```python
#示例 5-27 使用 partial 构建一个便利的 Unicode 规范化函数
>>> import unicodedata, functools
>>> nfc = functools.partial(unicodedata.normalize, 'NFC')
>>> s1 = 'café'
>>> s2 = 'cafe\u0301'
>>> s1, s2
('café', 'café')
>>> s1 == s2
False
>>> nfc(s1) == nfc(s2)
True
```

```python
#示例 5-28 把 partial 应用到示例 5-10 中定义的 tag 函数上
>>> from tagger import tag
>>> tag
<function tag at 0x10206d1e0> ➊
>>> from functools import partial
>>> picture = partial(tag, 'img', cls='pic-frame') ➋
>>> picture(src='wumpus.jpeg')
'<img class="pic-frame" src="wumpus.jpeg" />' ➌
>>> picture
functools.partial(<function tag at 0x10206d1e0>, 'img', cls='pic-frame') ➍
>>> picture.func ➎
<function tag at 0x10206d1e0>
>>> picture.args
('img',)
>>> picture.keywords
{'cls': 'pic-frame'}
➊ 从示例 5-10 中导入 tag 函数，查看它的 ID。
➋ 使用 tag 创建 picture 函数，把第一个定位参数固定为 'img'，把 cls 关键字参数固定
为 'pic-frame'。
➌ picture 的行为符合预期。
➍ partial() 返回一个 functools.partial 对象。5
➎ functools.partial 对象提供了访问原函数和固定参数的属性。
```

## 第 6 章 使用一等函数实现设计模式

### 6.1　案例分析：重构“策略”模式

#### 6.1.1　经典的“策略”模式

```python
#示例 6-1　实现 Order 类，支持插入式折扣策略
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.price * self.quantity

class Order: # 上下文
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

 def total(self):
    if not hasattr(self, '__total'): 
        self.__total = sum(item.total() for item in self.cart)
 return self.__total

 def due(self):
    if self.promotion is None:
        discount = 0
    else:
        discount = self.promotion.discount(self)
    return self.total() - discount

 def __repr__(self):
    fmt = '<Order total: {:.2f} due: {:.2f}>'
    return fmt.format(self.total(), self.due())

class Promotion(ABC): # 策略：抽象基类

 @abstractmethod
 def discount(self, order):
 """返回折扣金额（正值）"""

class FidelityPromo(Promotion): # 第一个具体策略
 """为积分为1000或以上的顾客提供5%折扣"""

 def discount(self, order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion): # 第二个具体策略
 """单个商品为20个或以上时提供10%折扣"""

 def discount(self, order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

class LargeOrderPromo(Promotion): # 第三个具体策略
 """订单中的不同商品达到10个或以上时提供7%折扣"""

 def discount(self, order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
```

```python
示例 6-2　使用不同促销折扣的 Order 类示例
 >>> joe = Customer('John Doe', 0) ➊
 >>> ann = Customer('Ann Smith', 1100)
 >>> cart = [LineItem('banana', 4, .5), ➋
 ... LineItem('apple', 10, 1.5),
 ... LineItem('watermellon', 5, 5.0)]
 >>> Order(joe, cart, FidelityPromo()) ➌
 <Order total: 42.00 due: 42.00>
 >>> Order(ann, cart, FidelityPromo()) ➍
 <Order total: 42.00 due: 39.90>
 >>> banana_cart = [LineItem('banana', 30, .5), ➎
 ... LineItem('apple', 10, 1.5)]
 >>> Order(joe, banana_cart, BulkItemPromo()) ➏
 <Order total: 30.00 due: 28.50>
 >>> long_order = [LineItem(str(item_code), 1, 1.0) ➐
 ... for item_code in range(10)]
 >>> Order(joe, long_order, LargeOrderPromo()) ➑
 <Order total: 10.00 due: 9.30>
 >>> Order(joe, cart, LargeOrderPromo())
 <Order total: 42.00 due: 42.00>
➊ 两个顾客：joe 的积分是 0，ann 的积分是 1100。
➋ 有三个商品的购物车。
➌ fidelityPromo 没给 joe 提供折扣。
➍ ann 得到了 5% 折扣，因为她的积分超过 1000。
➎ banana_cart 中有 30 把香蕉和 10 个苹果。
➏ BulkItemPromo 为 joe 购买的香蕉优惠了 1.50 美元。
➐ long_order 中有 10 个不同的商品，每个商品的价格为 1.00 美元。
➑ LargerOrderPromo 为 joe 的整个订单提供了 7% 折扣。
```

#### 6.1.2　使用函数实现“策略”模式

```python
#示例 6-3 Order 类和使用函数实现的折扣策略
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

 def __init__(self, product, quantity, price):
    self.product = product
    self.quantity = quantity
    self.price = price

 def total(self):
    return self.price * self.quantity

class Order: # 上下文

 def __init__(self, customer, cart, promotion=None):
    self.customer = customer
    self.cart = list(cart)
    self.promotion = promotion

 def total(self):
    if not hasattr(self, '__total'):
        self.__total = sum(item.total() for item in self.cart)
    return self.__total

 def due(self):
    if self.promotion is None:
        discount = 0
    else:
        discount = self.promotion(self) ➊
    return self.total() - discount

 def __repr__(self):
    fmt = '<Order total: {:.2f} due: {:.2f}>'
    return fmt.format(self.total(), self.due())
➋
def fidelity_promo(order): ➌
 """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
 """单个商品为20个或以上时提供10%折扣"""
 discount = 0
 for item in order.cart:
    if item.quantity >= 20:
        discount += item.total() * .1
return discount

 def large_order_promo(order):
 """订单中的不同商品达到10个或以上时提供7%折扣"""
 distinct_items = {item.product for item in order.cart}
 if len(distinct_items) >= 10:
    return order.total() * .07
 return 0
➊ 计算折扣只需调用 self.promotion() 函数。
➋ 没有抽象类。
➌ 各个策略都是函数。
```

```python
#示例 6-4　使用函数实现的促销折扣的 Order 类示例
 >>> joe = Customer('John Doe', 0) ➊
 >>> ann = Customer('Ann Smith', 1100)
 >>> cart = [LineItem('banana', 4, .5),
 ... LineItem('apple', 10, 1.5),
 ... LineItem('watermellon', 5, 5.0)]
 >>> Order(joe, cart, fidelity_promo) ➋
 <Order total: 42.00 due: 42.00>
 >>> Order(ann, cart, fidelity_promo)
 <Order total: 42.00 due: 39.90>
 >>> banana_cart = [LineItem('banana', 30, .5),
 ... LineItem('apple', 10, 1.5)]
 >>> Order(joe, banana_cart, bulk_item_promo) ➌
 <Order total: 30.00 due: 28.50>
 >>> long_order = [LineItem(str(item_code), 1, 1.0)
 ... for item_code in range(10)]
 >>> Order(joe, long_order, large_order_promo)
 <Order total: 10.00 due: 9.30>
 >>> Order(joe, cart, large_order_promo)
 <Order total: 42.00 due: 42.00>
➊ 与示例 6-1 一样的测试固件。
➋ 为了把折扣策略应用到 Order 实例上，只需把促销函数作为参数传入。
➌ 这个测试和下一个测试使用不同的促销函数。
```

#### 6.1.3　选择最佳策略：简单的方式

```python
#示例 6-5 best_promo 函数计算所有折扣，并返回额度最大的
 >>> Order(joe, long_order, best_promo) ➊
 <Order total: 10.00 due: 9.30>
 >>> Order(joe, banana_cart, best_promo) ➋
 <Order total: 30.00 due: 28.50>
 >>> Order(ann, cart, best_promo) ➌
 <Order total: 42.00 due: 39.90>
➊ best_promo 为顾客 joe 选择 larger_order_promo。
➋ 订购大量香蕉时，joe 使用 bulk_item_promo 提供的折扣。
➌ 在一个简单的购物车中，best_promo 为忠实顾客 ann 提供 fidelity_promo 优惠的折扣
```

```python
#示例 6-6 best_promo 迭代一个函数列表，并找出折扣额度最大的
promos = [fidelity_promo, bulk_item_promo, large_order_promo] ➊
def best_promo(order): ➋
 """选择可用的最佳折扣
 """
 return max(promo(order) for promo in promos) ➌
➊ promos 列出以函数实现的各个策略。
➋ 与其他几个 *_promo 函数一样，best_promo 函数的参数是一个 Order 实例。
➌ 使用生成器表达式把 order 传给 promos 列表中的各个函数，返回折扣额度最大的那个函数。
```

#### 6.1.4　找出模块中的全部策略

`globals()` :返回一个字典，表示当前的全局符号表。

```python
#示例 6-7　内省模块的全局命名空间，构建 promos 列表
promos = [globals()[name] for name in globals() ➊
    if name.endswith('_promo') ➋
    and name != 'best_promo'] ➌

def best_promo(order):
 """选择可用的最佳折扣
 """
    return max(promo(order) for promo in promos) ➍
➊ 迭代 globals() 返回字典中的各个 name。
➋ 只选择以 _promo 结尾的名称。
➌ 过滤掉 best_promo 自身，防止无限递归。
➍ best_promo 内部的代码没有变化。
```

```python
#示例 6-8　内省单独的 promotions 模块，构建 promos 列表
promos = [func for name, func in
 inspect.getmembers(promotions, inspect.isfunction)]
def best_promo(order):
 """选择可用的最佳折扣
 """
 return max(promo(order) for promo in promos)
```

inspect.getmembers 函数用于获取对象（这里是 promotions 模块）的属性，第二个参数是可选的判断条件（一个布尔值函数）。我们使用的是 inspect.isfunction，只获取模块中的函数。

### 6.2 “命令”模式

```python
#示例 6-9 MacroCommand 的各个实例都在内部存储着命令列表
class MacroCommand:
 """一个执行一组命令的命令"""
 def __init__(self, commands):
    self.commands = list(commands) # ➊
 def __call__(self):
    for command in self.commands: # ➋
        command()
➊ 使用 commands 参数构建一个列表，这样能确保参数是可迭代对象，还能在各个
MacroCommand 实例中保存各个命令引用的副本。
➋ 调用 MacroCommand 实例时，self.commands 中的各个命令依序执行。
```

## 第 7 章 函数装饰器和闭包

### 7.1　装饰器基础知识

```python
#假如有个名为 decorate 的装饰器：
@decorate
def target():
    print('running target()')

#上述代码的效果与下述写法一样：
def target():
    print('running target()')

target = decorate(target)
```

```python
#示例 7-1　装饰器通常把函数替换成另一个函数
>>> def deco(func):
... def inner():
... print('running inner()')
... return inner ➊
...
>>> @deco
... def target(): ➋
... print('running target()')
...
>>> target() ➌
running inner()
>>> target ➍
<function deco.<locals>.inner at 0x10063b598>
➊ deco 返回 inner 函数对象。
➋ 使用 deco 装饰 target。
➌ 调用被装饰的 target 其实会运行 inner。
➍ 审查对象，发现 target 现在是 inner 的引用。
```

### 7.2 Python何时执行装饰器

```python
#示例 7-2 registration.py 模块
registry = [] ➊
def register(func): ➋
    print('running register(%s)' % func) ➌
    registry.append(func) ➍
    return func ➎

@register ➏
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3(): ➐
    print('running f3()')

def main(): ➑
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main() ➒
➊ registry 保存被 @register 装饰的函数引用。
➋ register 的参数是一个函数。
➌ 为了演示，显示被装饰的函数。
➍ 把 func 存入 registry。
➎ 返回 func：必须返回函数；这里返回的函数与通过参数传入的一样。
➏ f1 和 f2 被 @register 装饰。
➐ f3 没有装饰。
➑ main 显示 registry，然后调用 f1()、f2() 和 f3()。
➒ 只有把 registration.py 当作脚本运行时才调用 main()。
```

```python
#输出:
$ python3 registration.py
running register(<function f1 at 0x100631bf8>)
running register(<function f2 at 0x100631c80>)
running main()
registry -> [<function f1 at 0x100631bf8>, <function f2 at 0x100631c80>]
running f1()
running f2()
running f3()
```

### 7.3　使用装饰器改进“策略”模式

```python
promos = [] #一个空列表

def promotion(promo_func): ➋
    promos.append(promo_func)
    return promo_func

@promotion ➌
def fidelity(order):
 """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
 """单个商品为20个或以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
 """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
         return order.total() * .07
    return 0

def best_promo(order): ➍
 """选择可用的最佳折扣
 """
 return max(promo(order) for promo in promos)
➊ promos 列表起初是空的。
➋ promotion 把 promo_func 添加到 promos 列表中，然后原封不动地将其返回。
➌ 被 @promotion 装饰的函数都会添加到 promos 列表中。
➍ best_promos 无需修改，因为它依赖 promos 列表。
```

### 7.4　变量作用域规则

```python
#使用 global 声明让解释器把 b 当成全局变量
>>> b = 6
>>> def f3(a):
... global b
... print(a)
... print(b)
... b = 9
...
>>> f3(3)
3
6
>>> b
9
>>> f3(3)
3
9
>>> b = 30
>>> b
30
>>>
```

### 7.5　闭包

```python
#示例 7-9 average.py：计算移动平均值的高阶函数
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
```

### 7.6 nonlocal声明

```python
#示例 7-13 计算移动平均值的高阶函数，不保存所有历史值，但有缺陷
def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return total / count
    return average
```

```python
>>> avg = make_averager()
>>> avg(10)
Traceback (most recent call last):
 ...
UnboundLocalError: local variable 'count' referenced before assignment
>>>
```

```python
#示例 7-14 计算移动平均值，不保存所有历史（使用 nonlocal 修正）
def make_averager():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
```

### 7.7　实现一个简单的装饰器

```python
#示例 7-16 使用 clock 装饰器
# clockdeco_demo.py
import time
from clockdeco import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__=='__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6)
```

```python
$ python3 clockdeco_demo.py
**************************************** Calling snooze(123)
[0.12405610s] snooze(.123) -> None
**************************************** Calling factorial(6)
[0.00000191s] factorial(1) -> 1
[0.00004911s] factorial(2) -> 2
[0.00008488s] factorial(3) -> 6
[0.00013208s] factorial(4) -> 24
[0.00019193s] factorial(5) -> 120
[0.00026107s] factorial(6) -> 720
6! = 720
```

### 7.8　标准库中的装饰器

```python
#示例 7-19 使用缓存实现，速度更快
import functools
from clockdeco import clock

@functools.lru_cache() # ➊
@clock # ➋
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))
➊ 注意，必须像常规函数那样调用 lru_cache。这一行中有一对括号：@functools.lru_cache()。这么做的原因是，lru_cache 可以接受配置参数，稍后说明。
➋ 这里叠放了装饰器：@lru_cache() 应用到 @clock 返回的函数上。
```

```python
这样一来，执行时间减半了，而且 n 的每个值只调用一次函数：
$ python3 fibo_demo_lru.py
[0.00000119s] fibonacci(0) -> 0
[0.00000119s] fibonacci(1) -> 1
[0.00010800s] fibonacci(2) -> 1
[0.00000787s] fibonacci(3) -> 2
[0.00016093s] fibonacci(4) -> 3
[0.00001216s] fibonacci(5) -> 5
[0.00025296s] fibonacci(6) -> 8
```

### 7.9　叠放装饰器

把 @d1 和 @d2 两个装饰器按顺序应用到 f 函数上，作用相当于 f = d1(d2(f))。

```python
@d1
@d2
def f():
    print('f')

等同于：
def f():
    print('f')

f = d1(d2(f))
```

#### 7.10　参数化装饰器

#### 7.10.1　一个参数化的注册装饰器

```python
#示例 7-23 为了接受参数，新的 register 装饰器必须作为函数调用
registry = set() ➊

def register(active=True): ➋
    def decorate(func): ➌
    print('running register(active=%s)->decorate(%s)'% (active, func))
    if active: ➍
        registry.add(func)
    else:
        registry.discard(func) ➎
    return func ➏
 return decorate ➐

@register(active=False) ➑
def f1():
    print('running f1()')

@register() ➒
def f2():
    print('running f2()')

def f3():
    print('running f3()')
➊ registry 现在是一个 set 对象，这样添加和删除函数的速度更快。
➋ register 接受一个可选的关键字参数。
➌ decorate 这个内部函数是真正的装饰器；注意，它的参数是一个函数。
➍ 只有 active 参数的值（从闭包中获取）是 True 时才注册 func。
➎ 如果 active 不为真，而且 func 在 registry 中，那么把它删除。
➏ decorate 是装饰器，必须返回一个函数。
➐ register 是装饰器工厂函数，因此返回 decorate。
➑ @register 工厂函数必须作为函数调用，并且传入所需的参数。
➒ 即使不传入参数，register 也必须作为函数调用（@register()），即要返回真正的装饰器 decorate。
```

## 第 8 章 对象引用、可变性和垃圾回收

### 8.1　变量不是盒子

```python
#示例 8-1　变量 a 和 b 引用同一个列表，而不是那个列表的副本
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> b
[1, 2, 3, 4]
```

### 8.2　标识、相等性和别名

```python
#示例 8-3 charles 和 lewis 指代同一个对象
>>> charles = {'name': 'Charles L. Dodgson', 'born': 1832}
>>> lewis = charles         
>>> lewis is charles
True
>>> id(charles), id(lewis) 
(4300473992, 4300473992)
>>> lewis['balance'] = 950 
>>> charles
{'name': 'Charles L. Dodgson', 'balance': 950, 'born': 1832}
lewis 是 charles 的别名
向 lewis 中添加一个元素相当于向 charles 中添加一个元素。
```

```python
#示例 8-4 alex 与 charles 比较的结果是相等，但 alex 不是 charles
>>> alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950} ➊
>>> alex == charles ➋
True
>>> alex is not charles ➌
True
➊ alex 指代的对象与赋值给 charles 的对象内容一样。
➋ 比较两个对象，结果相等，这是因为 dict 类的 __eq__ 方法就是这样实现的。
➌ 但它们是不同的对象。这是 Python 说明标识不同的方式：a is not b。
```

#### 8.2.1　在==和is之间选择

== 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识.

检查变量绑定的值是不是 None: `x is None`
否定的正确写法:`x is not None`

#### 8.2.2　元组的相对不可变性

```python
>>> t1 = (1, 2, [30, 40])   #t1 不可变，但是 t1[-1] 可变
>>> t2 = (1, 2, [30, 40])
>>> t1 == t2                #== 运算符比较两个对象的值（对象中保存的数据）
True
>>> id(t1[-1])              #查看 t1[-1] 列表的标识
4302515784
>>> t1[-1].append(99)       #修改 t1[-1] 列表
>>> t1
(1, 2, [30, 40, 99])
>>> id(t1[-1]) 
4302515784
>>> t1 == t2
False
```

### 8.3　默认做浅复制

```python
>>> l1 = [3, [55, 44], (7, 8, 9)]
>>> l2 = list(l1)       #list(l1) 创建 l1 的副本
>>> l2
[3, [55, 44], (7, 8, 9)]
>>> l2 == l1
True
>>> l2 is l1
False                   #但是二者指代不同的对象。
```

```python
#使用 copy 和 deepcopy 产生的影响
>>> import copy
>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
>>> bus2 = copy.copy(bus1)
>>> bus3 = copy.deepcopy(bus1)
>>> id(bus1), id(bus2), id(bus3)
(4301498296, 4301499416, 4301499752) ➊
>>> bus1.drop('Bill')
>>> bus2.passengers
['Alice', 'Claire', 'David'] ➋
>>> id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
(4302658568, 4302658568, 4302657800) ➌
>>> bus3.passengers
['Alice', 'Bill', 'Claire', 'David'] ➍

➊ 使用 copy 和 deepcopy，创建 3 个不同的 Bus 实例。
➋ bus1 中的 'Bill' 下车后，bus2 中也没有他了。
➌ 审查 passengers 属性后发现，bus1 和 bus2 共享同一个列表对象，因为 bus2 是 bus1 的
浅复制副本。
➍ bus3 是 bus1 的深复制副本，因此它的 passengers 属性指代另一个列表。
```

### 8.6　弱引用

弱引用是可调用的对象，返回的是被引用的对象；如果所指对象不存在了，返回 None

```python
>>> import weakref

>>> a_set = {0, 1}
>>> wref = weakref.ref(a_set)   #创建弱引用对象 wref
>>> wref 
<weakref at 0x100637598; to 'set' at 0x100636748>
>>> wref()      #调用 wref() 返回的是被引用的对象，{0, 1}。因为这是控制台会话，所以{0, 1} 会绑定给 _ 变量
{0, 1}
>>> a_set = {2, 3, 4} 
>>> wref()      #调用 wref() 依旧返回 {0, 1}
{0, 1}
>>> wref() is None  #计算这个表达式时，{0, 1} 存在，因此 wref() 不是 None。但是，随后 _ 绑定到结果值False。现在 {0, 1} 没有强引用了。
False
>>> wref() is None  #因为 {0, 1} 对象不存在了，所以 wref() 返回 None
True
```

### 8.7 Python对不可变类型施加的把戏

```python
#示例 8-20 使用另一个元组构建元组，得到的其实是同一个元组
>>> t1 = (1, 2, 3)
>>> t2 = tuple(t1)
>>> t2 is t1    #t1 和 t2 绑定到同一个对象
True
>>> t3 = t1[:]
>>> t3 is t1
True
```

## 第 9 章 符合Python风格的对象

### 9.1　对象表示形式

repr()  以便于开发者理解的方式返回对象的字符串表示形式。

str()   以便于用户理解的方式返回对象的字符串表示形式。

### 9.5　格式化显示

```python
>>> brl = 1/2.43 # BRL到USD的货币兑换比价
>>> brl
0.4115226337448559
>>> format(brl, '0.4f')     # 用format()函数 把brl 以(f)浮点数 并保留小数点后4位
'0.4115'
>>> '1 BRL = {rate:0.2f} USD'.format(rate=brl)      #把brl传给代换字段
'1 BRL = 0.41 USD'
```

```python
#b 和 x 分别表示二进制和十六进制的 int 类型，f 表示小数形式的 float 类型，而 % 表示百分数形式
>>> format(42, 'b')
'101010'
>>> format(2/3, '.1%')
'66.7%'
```

```python
>>> from datetime import datetime
>>> now = datetime.now()
>>> format(now, '%H:%M:%S')
'18:49:05'
>>> "It's now {:%I:%M %p}".format(now)
"It's now 06:49 PM"
```

```python
>>> v1 = Vector2d(3, 4)
>>> format(v1)
'(3.0, 4.0)'
```

### 9.6　可散列的Vector2d

```python
class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)     #使用两个前导下划线,把属性标记为私有的
        self.__y = float(y)

 @property                      #@property 装饰器把读值方法标记为特性
 def x(self):                   #读值方法与公开属性同名，都是 x
    return self.__x 

 @property 
 def y(self):
    return self.__y

 def __iter__(self):
    return (i for i in (self.x, self.y)) 
```

```python
#示例 9-8 vector2d_v3.py：实现 __hash__ 方法
# 在Vector2d类中定义
def __hash__(self):
    return hash(self.x) ^ hash(self.y)

```

```python
#添加 __hash__ 方法之后，向量变成可散列的了：
>>> v1 = Vector2d(3, 4)
>>> v2 = Vector2d(3.1, 4.2)
>>> hash(v1), hash(v2)
(7, 384307168202284039)
>>> set([v1, v2])
{Vector2d(3.1, 4.2), Vector2d(3.0, 4.0)}
```

### 9.7 Python的私有属性和“受保护的”属性

```python
以 __mood 的形式（两个前导下划线，尾部没有或最多有一个下划线）命名实例属性Python 会把属性名存入实例的 __dict__ 属性中，而且会在前面加上一个下划线和类名.这个语言特性叫名称改写.(__mood 会变成 _Dog__mood)
```

```python
#示例 9-10 私有属性的名称会被“改写”，在前面加上下划线和类名
>>> v1 = Vector2d(3, 4)
>>> v1.__dict__
{'_Vector2d__y': 4.0, '_Vector2d__x': 3.0}
>>> v1._Vector2d__x
3.0
```

### 9.8　使用__slots__类属性节省空间

```python
#示例 9-11 vector2d_v3_slots.py：只在 Vector2d 类中添加了 __slots__ 属性
class Vector2d:
 __slots__ = ('__x', '__y') #在类中定义 __slots__ 属性的目的是告诉解释器：“这个类中的所有实例属性都在这儿,Python 会在各个实例中使用类似元组的结构存储实例变量，从而避免使用消耗内存的 __dict__ 属性
 typecode = 'd'
```

## 第 1 1 章 接口：从协议到抽象基类

序列协议的重要性，如果没有 __iter__ 和 __contains__ 方法，Python 会调用__getitem__ 方法，设法让迭代和 in 运算符可用

```python
#random.shuffle 函数用法如下：
>>> from random import shuffle
>>> l = list(range(10))
>>> shuffle(l)
>>> l
[5, 2, 9, 7, 8, 3, 1, 4, 0, 6]
```

可变的序列还必须提供 __setitem__ 方法

```python
#示例 11-6 为 FrenchDeck 打猴子补丁，把它变成可变的，让 random.shuffle 函数能处理（接续示例 11-5）
>>> def set_card(deck, position, card): #定义一个函数，它的参数为 deck、position 和 card
... deck._cards[position] = card
...
>>> FrenchDeck.__setitem__ = set_card #把那个函数赋值给 FrenchDeck 类的 __setitem__ 属性
>>> shuffle(deck) #可以打乱了,因为 FrenchDeck 实现了可变序列协议所需的方法
>>> deck[:5]
[Card(rank='3', suit='hearts'), Card(rank='4', suit='diamonds'), Card(rank='4',
suit='clubs'), Card(rank='7', suit='hearts'), Card(rank='9', suit='spades')]
```

### 11.6　标准库中的抽象基类

#### 11.6.2 抽象基类的数字塔

想检查一个数是不是整数，可以使用 isinstance(x, numbers.Integral)

果一个值可能是浮点数类型，可以使用 isinstance(x, numbers.Real) 检查

### 11.7　定义并使用一个抽象基类

Tombola 抽象基类有四个方法，其中两个是抽象方法。
.load(...)：把元素放入容器。
.pick()：从容器中随机拿出一个元素，返回选中的元素。

另外两个是具体方法。
.loaded()：如果容器中至少有一个元素，返回 True。
.inspect()：返回一个有序元组，由容器中的现有元素构成，不会修改容器的内容（内部的顺序不保留）。

## 第 1 2 章 继承的优缺点

### 12.1　子类化内置类型很麻烦

```python
#示例 12-1 内置类型 dict 的 __init__ 和 __update__ 方法会忽略我们覆盖的 __setitem__ 方法
>>> class DoppelDict(dict):
... def __setitem__(self, key, value):
... super().__setitem__(key, [value] * 2) #DoppelDict.__setitem_方法会重复存入的值
...
>>> dd = DoppelDict(one=1) # 'one' 的值没有重复
>>> dd
{'one': 1}
>>> dd['two'] = 2 #[] 运算符会调用我们覆盖的 __setitem__ 方法，按预期那样工作：'two' 对应的是两个重复的值，即 [2, 2]。
>>> dd
{'one': 1, 'two': [2, 2]}
>>> dd.update(three=3) # 继承自 dict 的 update 方法也不使用我们覆盖的 __setitem__ 方法：'three' 的值没有重复
>>> dd
{'three': 3, 'one': 1, 'two': [2, 2]}
```

## 第 1 3 章 正确重载运算符

### 13.2　一元运算符

```python
-（__neg__）
一元取负算术运算符。如果 x 是 -2，那么 -x == 2.

+（__pos__）
一元取正算术运算符。通常，x == +x，但也有一些例外.

~（__invert__）
对整数按位取反，定义为 ~x == -(x+1)。如果 x 是 2，那么 ~x == -3.
```

## 第 1 4 章 可迭代的对象、迭代器和生成器

迭代器用于从集合中取出元素.

`list(range(10))` :让 range() 函数返回列表

```python
序列可以迭代的原因：iter函数
解释器需要迭代对象 x 时，会自动调用 iter(x).
内置的 iter 函数有以下作用。
(1) 检查对象是否实现了 __iter__ 方法，如果实现了就调用它，获取一个迭代器。
(2) 如果没有实现 __iter__ 方法，但是实现了 __getitem__ 方法，Python 会创建一个迭代器，尝试按顺序（从索引 0 开始）获取元素。
(3) 如果尝试失败，Python 抛出 TypeError 异常，通常会提示“C object is not iterable”（C对象不可迭代），其中 C 是目标对象所属的类。
```

检查对象x能否迭代,调用 iter(x) 函数.

可迭代的对象:使用 iter 内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的 __iter__方法，那么对象就是可迭代的;序列都可以迭代;实现了 __getitem__ 方法，而且其参数是从零开始的索引，这种对象也可以迭代.

可迭代的对象和迭代器之间的关系：Python 从可迭代的对象中获取迭代器.

标准的迭代器接口有两个方法:
__next__(返回下一个可以的元素,没有元素了抛出 StopIteration 异常)
__iter__(返回 self，以便在应该使用可迭代对象的地方使用迭代器，例如在 for 循环中)

`isinstance(x, abc.Iterator)` 检查对象 x 是否为迭代器

```python
>>> s3 = Sentence('Pig and Pepper') # 创建一个 Sentence 实例 s3
>>> it = iter(s3)                   # 从 s3 中获取迭代器
>>> it # doctest: +ELLIPSIS
<iterator object at 0x...>
>>> next(it)                        # 调用 next() 函数获取下一个单词
'Pig'
>>> next(it)
'and'
>>> next(it)
'Pepper'
>>> next(it)                        # 没有单词了,迭代器抛出 StopIteration 异常
Traceback (most recent call last):
 ...
StopIteration
>>> list(it)                        # 到头了,迭代器没用了
[]
>>> list(iter(s3))                  # 想再次迭代,要重新构建迭代器
['Pig', 'and', 'Pepper']

```

### 14.4 生成器函数

只要 Python 函数的定义体中有 yield 关键字，该函数就是生成器函数。调用生成器函数时，会返回一个生成器对象.

### 14.6 Sentence类第5版：生成器表达式

```python
#示例 14-8 先在列表推导中使用 gen_AB 生成器函数，然后在生成器表达式中使用
>>> def gen_AB(): 
... print('start')
... yield 'A'
... print('continue')
... yield 'B'
... print('end.')
...
>>> res1 = [x*3 for x in gen_AB()] # 列表推导迫切地迭代 gen_AB() 函数生成的生成器对象产出的元素：'A' 和 'B'
start
continue
end.
>>> for i in res1: # 这个 for 循环迭代列表推导生成的 res1 列表
... print('-->', i)
...
--> AAA
--> BBB
>>> res2 = (x*3 for x in gen_AB()) # 把生成器表达式返回的值赋值给 res2。只需调用 gen_AB() 函数
>>> res2 # res2 是一个生成器对象
<generator object <genexpr> at 0x10063c240>
>>> for i in res2: # 只有 for 循环迭代 res2 时，gen_AB 函数的定义体才会真正执行
... print('-->', i)
...
start
--> AAA
continue
--> BBB
end.
```

### 14.8　另一个示例：等差数列生成器

```python
#示例 14-10　演示 ArithmeticProgression 类的用法
>>> ap = ArithmeticProgression(0, 1, 3)
>>> list(ap)
[0, 1, 2]
>>> ap = ArithmeticProgression(1, .5, 3)
>>> list(ap)
[1.0, 1.5, 2.0, 2.5]
>>> ap = ArithmeticProgression(0, 1/3, 1)
>>> list(ap)
[0.0, 0.3333333333333333, 0.6666666666666666]
>>> from fractions import Fraction
>>> ap = ArithmeticProgression(0, Fraction(1, 3), 1)
>>> list(ap)
[Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
>>> from decimal import Decimal
>>> ap = ArithmeticProgression(0, Decimal('.1'), .3)
>>> list(ap)
[Decimal('0.0'), Decimal('0.1'), Decimal('0.2')]
```

使用itertools模块生成等差数列

```python
>>> import itertools
>>> gen = itertools.count(1, .5)
>>> next(gen)
1
>>> next(gen)
1.5
>>> next(gen)
2.0
>>> next(gen)
2.5
```

```python
>>> gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
>>> list(gen)
[1, 1.5, 2.0, 2.5]
```

## 第 1 5 章 上下文管理器和else块

### 15.2　上下文管理器和with块

上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。with 语句开始运行时，会在上下文管理器对象上调用 __enter__ 方法。with 语句运行结束后，会在上下文管理器对象上调用 __exit__ 方法
