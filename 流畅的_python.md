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

我们需要单独写一个方法用来随机抽取一张纸牌吗？没必要，Python 已经内置了从一个序
列中随机选出一个元素的函数 random.choice，我们直接把它用在这一摞纸牌实例上就好：

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
