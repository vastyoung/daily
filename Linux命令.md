
# `Linux命令行笔记:`

## 第一章

`exit` :终止一个终端会话

`date` :显示当前日期和时间

`cal` :显示当前月份的日历

`df` :查看磁盘剩余空间的数量

`free` :显示空闲内存的数量

## 第二章:文件系统的跳转

`pwd`: 打印出当前工作目录名

`cd`: 更改目录

`cd .` : 工作目录

`cd ..` : 切换到当前目录的上一级目录

`cd -` : 更改工作目录到先前的工作目录

## 第三章:探究操作系统

`ls` : 列出目录内容

`ls -a` : 列出目录内容(包含隐藏文件)

`ls -al` : 列出所有文件，包括隐藏文件,长模式输出

`ls -l` : 以长模式输出

`ls -t` :  按照修改时间来排序

`ls -lt` :  选项按文件修改时间的先后来排序长模式输出

 `ls -lt --reverse` : 以相反的顺序输出

`ls -h` : 以合适的单位显示文件的大小,方便阅读

`ls -r` :  以相反的顺序来显示结果

`file` : 确定文件类型

`less` : 浏览文件内容

记得复制和粘贴技巧！如果你正在使用鼠标，双击文件名，来复制它，然后按下鼠标中键，
粘贴文件名到命令行中。

## 第四章:操作文件和目录

`cp` : 复制文件和目录

`mv` : 移动/重命名文件和目录

`mkdir` : 创建目录

`rm`:删除文件和目录

`ln` :创建硬链接和符号链接

### 4.1 :通配符

`*` :匹配任意多个字符（包括零个或一个）

`Data???`: 以“Data”开头，其后紧接着 3 个字符的文件

`[abc]*`: 文件名以”a”,”b”, 或”c” 开头的文件

` ls /usr/bin/u* ` :查看目录 /usr/bin 中，所有以小写字母 ‘u’ 开头的文
件

`cp -a` :复制文件和目录，以及它们的属性，包括所有权和权限

`cp -u` :当把文件从一个目录复制到另一个目录时，仅复制目标目录
中不存在的文件

`cp -r`  复制目录及目录中的内容

`cp dir1/* dir2` 使用一个通配符，在目录 dir1 中的所有文件都被复制到目
录 dir2 中。dir2 必须已经存在。

`mv test1/* test2`  把test1下面的所有文件移动到test2下面

`mv dir1/fun dir2` :  把dir1下面的fun文件移动到dir2下面

`mv dir2/fun .` :   把dir2下面的fun文件移动到当前工作目录

 `ls -li` :展示（文件索引节点）的信息

`history` : 查看之前输入的命令历史

 `whoami` :查看当前用户

`who` :显示当前登录系统的用户

## 第五章:使用命令

`type` :显示命令的类型

`which` :显示一个可执行程序的位置

`help` :得到 shell 内建命令的帮助文档

`mkdir --help` :显示mkdir用法信息

`man` :显示命令手册页

`apropos` :显示一系列适合的命令

`info` :显示命令 info

`whatis` :显示一个命令的简洁描述

`alias` :创建命令别名

`alias foo='cd /usr'` :创建foo别名(alias foo='cd /usr/bin ; ls -l')

`type foo` :查看别名

`unalias foo` :删除foo别名

## 第六章:重定向

`ls -l /usr/bin > ls-output.txt` :ls -l命令的运行结果输送到文件ls-output.txt中

`> ls-output.txt` :清空或创建一个新的空文件

文件流的前三个称作标准输入、输出和错误，shell 内部分别将其称为文件描述符 0、1 和 2。

`ls -l /usr/bin >> ls-output.txt` :重定向结果追加到ls-output.txt文件内容后面，

`ls -l /bin/usr 2> ls-error.txt` :重定向标准错误到文件 ls-error.txt

`ls -l /bin/usr > ls-output.txt 2>&1` :同时重定向标准输出和标准错误到ls-output.txt文件

`>ls-output.txt 2>&1` :重定向标准错误到文件 ls-output.txt

`2>&1 >ls-output.txt` :标准错误定向到屏幕

`ls -l /bin/usr &> ls-output.txt` :(表示法 &>)重定向标准输出和错误到文件 lsoutput.txt

`ls -l /bin/usr 2> /dev/null` :隐瞒命令错误信息

`cat` :连接文件

 `cat ls-output.txt` :显示ls-output文件

`cat > lazy_dog.txt` :创建一个叫做lazy_dog.txt的文件

`cat < lazy_dog.txt` :使用<重定向操作符，我们把标准输入源从键盘改到文件 lazy_dog.tx

`ls -l /usr/bin | less` :

`ls /bin /usr/bin | sort | less` :把目录/bin 和/usr/bin 中的可执行程序都联合在一起，再把它们排序，然后浏览执行结果

`sort` :排序文本行

`ls /bin /usr/bin | sort | uniq | less` :们使用 uniq 从 sort 命令的输出结果中，来删除任何重复行

`ls /bin /usr/bin | sort | uniq -d | less` :看到重复的数据列表

`uniq` :报道或省略重复行

`wc` : 打印文件中换行符，字，和字节个数

`wc ls-output.txt` :显示文件所包含的行数、字数和字节数

`ls /bin /usr/bin | sort | uniq | wc -l` :限制命令输出只能报道行数

`grep` :打印匹配行

`ls /bin /usr/bin | sort | uniq | grep zip` :找到文件名中包含单词 “zip” 的所有文件

`head` :输出文件第一部分

`head -n 5 ls-output.txt` :(可以通过 “-n” 选项来调整命令打印的行数)打印文件ls-output.txt的前五行

`tail` : 输出文件最后一部分

`tail -n 5 ls-output.txt` :打印文件ls-output.txt的末尾五行

`ls /usr/bin | tail -n 5` :列出/usr/bin目录内容后五行

`tail -f /var/log/messages` :使用 “-f” 选项，tail 命令继续监测这个文件，当新的内容添加到文件后，它们会立即出现在屏幕上。这会一直继续下去直到你输入 Ctrl-c

`tee` : 从标准输入读取数据，并同时写到标准输出和文件

`ls /usr/bin | tee ls.txt | grep zip` :

## 第七章:从 shell 眼中看世界

`echo` :显示一行文本

`echo this is a test` :显示this is a test文本

`echo d*` :显示所有以d开头的文本

 `echo ~` :展示当前用户的家目录

`echo $((2 + 2))` :加法运算

`echo $(($((5**2)) * 3))` :5 的平方乘以 3

`echo Front-{A,B,C}-Back` :从一个包含花括号的模式中创建多个文本字符串

`echo Number_{1..5}` :创建多个文本字符串

`echo {a..z}` :正序排列的字母区间

`echo a{A{1,2},B{3,4}}b` :花括号嵌套(aA1b aA2b aB3b aB4b)

`mkdir {2007..2009}-0{1..9} {2007..2009}-{10..12}` :“年－月” 形式命名的目录

 `echo $USER` :USER 中的内容包含你的用户名

`printenv | less` :

`echo $(ls)` :把一个命令的输出作为一个展开模式来使用

`ls -l $(which cp)` :查看指令"cp"的绝对路径以长模式输出

`file $(ls /usr/bin/* | grep zip)` :

`ls -l`which cp`` :(使用倒引号来代替美元符号和括号)查看指令"cp"的绝对路径以长模式输出

`echo this is a  test` :(this is a test)利用单词分割删除掉 echo 命令的参数列表中多余的空格

`echo The total is $100.00` :(The total is 00.00)参数展开把 $1 的值替换为一个空字符串，因为 1 是没有定义的变量

`ls -l "two words.txt"` :使用双引号，我们可以阻止单词分割

`echo "$USER $((2+2)) $(cal)"` :(Administrator 4     November 2021)

`echo "this is a    test"` :(this is a      test)单词分割被禁止，内嵌的空格也不会被当作界定符，它们成为参数的一部分

`echo $(cal)` :显示当前月份的日历

`echo text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER` :(text /home/me/ls-output.txt a b foo 4 me)无引用

 `echo "text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER"` :(text ~/*.txt {a,b} foo 4 me)双引号

`echo 'text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER'` :(text ~/*.txt {a,b} $(echo foo) $((2+2)) $USER)单引号

`echo "The balance for user $USER is: $5.00"` :(The balance for user Administrator is: .00)

 `echo "The balance for user $USER is: \$5.00"` :(The balance for user me is: $5.00)引用单个字符。我们可以在字符之前加上一个反斜杠，在这里叫做转义字符

`mv bad\&filename good_filename` :允许反斜杠字符出现，输入 “\” 来转义。注意在单引号中，反斜杠失去它的特殊含义，它被看作普通字符

## 第八章:键盘高级操作

`clear` :清空屏幕

`history` :显示历史列表内容

### 8.1 :移动光标

`Ctrl-a` :移动光标到行首

`Ctrl-e` :移动光标到行末
