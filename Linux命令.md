
# `Linux命令行笔记:`

`ssh itzou@192.168.200.128` :登录到itzou@192.168.200.130

`ifconfig` :查看linux ip地址

`g`按键 :跳转到文件头部

`SHIFT+g` :跳转到文件尾部

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

`Ctrl-f` :光标前移一个字符；和右箭头作用一样

`Ctrl-b` :光标后移一个字符；和左箭头作用一样

`Alt-f` :光标前移一个字

`Alt-b` :光标后移一个字

`Ctrl-l` :清空屏幕,移动光标到左上角。和clear 命令一样

### 8.2 修改文本

`Ctrl-d` :删除光标位置的字符

`Ctrl-t` :光标位置的字符和光标前面的字符互换位置

`Alt-t` :光标位置的字和其前面的字互换位置

`Alt-l` :把从光标位置到字尾的字符转换成小写字母

`Alt-u` :把从光标位置到字尾的字符转换成大写字母

### 8.3 剪切和粘贴文本

`Ctrl-k` :剪切从光标位置到行尾的文本

`Ctrl-u` :剪切从光标位置到行首的文本

`Alt-d` :剪切从光标位置到词尾的文本

`Alt-Backspace` :剪切从光标位置到词头的文本。如果光标在一个单词的开头，剪切前一个单词

`Ctrl-y` :把剪切环中的文本粘贴到光标位置

### 8.4 自动补全

`tab键` :自动补全

`Alt-?` :显示可能的自动补全列表(也可以通过按两次 tab 键)

`Alt-*` :插入所有可能的自动补全,当你想要使用多个可能的匹配项时，这个很有帮助

### 8.5 搜索历史命令

`history | less` :浏览你所输入命令的历史列表

`history | grep /usr/bin` :找出和/usr/bin 这一目录相关的命令

`(reverse-i-search)`/usr/bin': ls -l /usr/bin > ls-output.txt` :(Ctrl-r)反向增量搜索(我们可以按下 Enter 键来执行这个命令，或者我们可以按下 Ctrl-j 复制这个命令到我们当前的命令行)

`Ctrl-p` :移动到上一个历史条目。类似于上箭头按键

`Ctrl-n` :移动到下一个历史条目。类似于下箭头按键

`Alt-<` :移动到历史列表开头

`Alt->` :移动到历史列表结尾

`Ctrl-r` :反向增量搜索。从当前命令行开始，向上增量搜索

`Alt-p` :反向搜索，非增量搜索。（输入要查找的字符串，按下 Enter来执行搜索）

`Alt-n` :向前搜索，非增量

`Ctrl-o` :执行历史列表中的当前项，并移到下一个

### 8.6 历史命令展开

`!!` :重复最后一次执行的命令

`!numbe` :重复历史列表中第 number 行的命令

`!string` :重复最近历史列表中，以这个字符串开头的命令

`!?string` :重复最近历史列表中，包含这个字符串的命令

## 第九章:权限

### 9.1 拥有者、组成员和其他人

`id` :显示用户身份号

`chmod` :更改文件模式

`umask` :设置默认的文件权限

`su` :以另一个用户的身份来运行 shell

`su - itzou` :变更帐号为 itzou并改变工作目录至 itzou的家目录

`sudo` :以另一个用户的身份来执行命令

`chown` :更改文件所有者

`chgrp` :更改文件组所有权

`passwd` :更改用户密码

### 9.2 读取、写入和执行

`-rw-rw-r--` :前十个字符是文件的属性

`-` :以-开头的文件是一个普通文件

`d` :以d开头的是一个目录

`l` :以l开头是一个符号链接''(文件属性总是''rwxrwxrwx'')

`c` :这种文件类型是指按照字节流来处理数据的设备

`b` :这种文件类型是指按照数据块来处理数据的设备，例如一个硬盘或者 CD-ROM 盘

剩下的九个字符叫做文件模式，代表着文件所有者、文件组所有者和其他人的读、写和执行权限

`rwx` :可读、可写、可执行

通过使用 3 个八进制数字，我们能够设置文件所有者、用户组和其他人的权限

0 (-–)

1 (--x)

2 (-w-)

3 (-wx)

4 (r--)

5 (r-x)

6 (rw-)

7 (rwx)

`chmod 600 foo.txt` :将文件权限改为600(设置文件所有者的权限为读写权限，而删除用户组和其他人的所有权限)

chmod 命令支持一种符号表示法通过字符“u”、“g”、“o”和“a”的组合来指定要影响的对象

`u` :''user''的简写，意思是文件或目录的所有者

`g` :用户组

`o` :''others''的简写，意思是其他所有的人

`a` :all'' 的简写，是”u”, ”g” 和“o”三者的联合

如果没有指定字符，则假定使用 “all”。执行的操作可能是一个“＋”字符，表示加上一个权限，一个“－”，表示删掉一个权限，或者是一个“＝”，表示只有指定的权限可用，其它所有的权限被删除

`u+x` :为文件所有者添加可执行权限

`u-x` :删除文件所有者的可执行权限

`+x` :为文件所有者，用户组，和其他所有人添加可执行权限。等价于 a+x

`o-rw` :除了文件所有者和用户组，删除其他人的读权限和写权限

`go=rw` :给文件所属的组和文件所属者/组以外的人读写权限。如果文件所属组或其他人已经拥有执行的权限，执行权限将被移除

`u+x,go=rw` :给文件拥有者执行权限并给组和其他人读和执行的权限,多种设定可以用逗号分开

`exit` :登出返回到原来的 shel

`chown runoob:runoobgroup file1.txt` :将文件 file1.txt 的拥有者设为 runoob，群体的使用者 runoobgroup

`bob` :把文件所有者从当前属主更改为用户 bob

`bob:users` :把文件所有者改为用户 bob，文件用户组改为用户组 users

`:admins` :把文件用户组改为组 admins，文件所有者不变

`bob:` :文件所有者改为用户 bob，文件用户组改为用户 bob 登录系统时所属的用户组

`sudo chown itzou:itzou a.txt`  :用sudo命令将文件a.txt的拥有者设为 itzou，群体的使用者 itzou

## 第十章 进程

`ps` :列出与当前终端会话相关的进程

`ps x` :展示所有进程

标题为 STAT 。STAT 是 “state” 的简写，它揭示了进程当前状态

`R` :运行中。这意味着，进程正在运行或准备运行

`S` :正在睡眠。进程没有运行，而是，正在等待一个事件，比如说，一个按键或者网络分组

`D` :不可中断睡眠。进程正在等待 I/O，比方说，一个磁盘驱动器的 I/O

`T` :已停止. 已经指示进程停止运行

`Z` :一个死进程或“僵尸”进程。这是一个已经终止的子进程，但是它的父进程还没有清空它。（父进程没有把子进程从进程表中删除）

`<` :一个高优先级进程,它占用了比较多的 CPU 时间，这样就给其它进程留下很少时间

`N` :低优先级进程,只有当其它高优先级进程被服务了之后，才会得到处理器时间

`ps aux` :这个选项组合，能够显示属于每个用户的进程信息,通过这些选项，我们得到这些额外的列

`USER` :用户 ID. 进程的所有者

`%CPU` :以百分比表示的 CPU 使用率

`%MEM` :以百分比表示的内存使用率

`VSZ` :虚拟内存大小

`RSS` :进程占用的物理内存的大小，以千字节为单位

`START` :进程启动的时间。若它的值超过 24 小时，则用天表示

`top` :命令动态查看进程

`xlogo &` :启动一个程序并让它立即在后台运行

`jobs` :列出从我们终端中启动了的任务

`fg %1` :恢复程序1到前台运行

`bg %1` :把程序1移动到后台

`kill 28401` :杀死程序28401

`kill -HUP 28401` :挂起进程28401(重启)

`kill -INT 28401` :中断进程28401

`kill -KILL 28401` :彻底杀死进程

`kill -TERM 28401`:终止进程28401

`kill -CONT 28401`:(恢复一个停止的进程)恢复进程的运行28401

`kill -STOP 28401` :停止进程

`kill -1 13546` :给进程13546发送HUP信号

`pstree` :输出一个树型结构的进程列表

## 第十一章 shell 环境

`printenv` :打印部分或所有的环境变量

`printenv | less` :浏览所有环境变量

`printenv USER` :列出叫做USER变量的值

`set | less` :按照首字母顺序排列查看环境变量

`echo $HOME` :查看一个变量的内容

`alias` :查看别名

`export` :导出环境变量，让随后执行的程序知道

有两种 shell 会话类型：一个是登录 shell 会话，另一个是非登录 shell 会话

文本编辑器分为两种基本类型：图形化的和基于文本的编辑器

`gedit some_file` :启动 gedit 文本编辑器，同时加载名为 “some_file” 的文件

`cp .bashrc .bashrc.bak` :创建文件.bashrc 的备份文件

备份文件的名字无关紧要，只要选择一个容易理解的文件名。扩展名 “.bak”、”.sav”、“.old”
和 “.orig” 都是用来指示备份文件的流行方法

`nano .bashrc` :启动 nano 编辑器(输入 Ctrl-x 来退出 nano, Ctrl-o保存我们的修改)

文本行       :含义

`umask 0002` :设置掩码来解决共享目录的问题。

`export HISTCONTROL=ignoredups` :使得 shell 的历史记录功能忽略一个命令，如果相同的命令已被记录。

`export HISTSIZE=1000` :增加命令历史的大小从默认的 500 行扩大到1000 行

`alias l.=’ls -d .* --color=auto’` :创建个新命令，叫做’l.’，这个命令会显示所有以点开头的目录项。

`alias ll=’ls -l --color=auto’` :创建一个做’ll’ 的命令，这个命令会显示长格式目录列表。

`source .bashrc` :重新读取修改过的.bashrc 文件

## 十二 vi

vi 很多系统都预装

vi 轻量级且执行快

`vi` :启动vi(vim)

`:q` :退出vi

`:q!` :由于某种原因，vi 不能退出（通常因为们对文件做了修改，却没有保存文件）。通过给命加上叹号，我们可以告诉 vi 我们真要退出 vi

如果你在 vi 中“迷失”了，试着按下 Esc 键两次来回到普通模式

在你的.bashrc 文件中添加 alias vi='vim'

`vi foo.txt` :vi 创建新文件

在文件中添加文本，我们需要先进入插入模式。按下 “i” 键进入插入模式

若要退出插入模式返回命令模式，按下 Esc 按键

`:w` :保存我们的编辑

`l or 右箭头` :向右移动一个字符

`h or 左箭头` :向左移动一个字符

`j or 下箭头` :向下移动一行

`k or 上箭头` :向上移动一行\

`0 (零按键)` :移动到当前行的行首

`^` :移动到当前行的第一个非空字符

`$` :移动到当前行的末尾

`u`按键 :撤销你所做的最后一次修改

`a`按键 :进入插入模式

`x`按键 :删除当前字符

`dd`按键 :删除当前行

`d0`按键 :删除从光标位置开始到当前行的行首位置

`yy`按键 :复制当前行

`y0`按键 :复制从当前光标位置到行首

`p`按键 :粘贴

`f`:命令能搜索一特定行

`/Line` :查找整个文件中Line

`n` :命令来重复先前的查找

`ex` :命令来执行替换

`:%s/Line/line/g` :整个文件中的单词"Line"改
为"line"

每部分的含义

`:` :冒号字符运行一个 ex 命令

`%` :指定要操作的行数。% 是一个快捷方式，表从第一行到最后一行,操作范围也可以用 1,5 来代替（因为我们的文件只有 5 行文本）

`s` :指定操作。在这种情况下是，替换（查找与替代）

`/Line/line` :查找类型与替代文本

`g` :这是“全局”的意思，意味着对文本行中所有匹配的字符串执行查找和替换操作。如果省略 g，则只替换每个文本行中第一个匹配的字符串

`:%s/line/Line/gc` :以指定一个需要用户确认的替换命令。通过添加一个 “c” 字符到这个命令的末尾，来完成这个替换命令

这个命令会把我们的文件恢复先前的模样；然而，在执行每个替换命令之前，vi 会停下来，通过下面的信息，来要求我们确认这个替换

`replace with Line (y/n/a/q/l/^E/^Y)?` :括号中的每个字符都是一个可能的选择

`y` :执行替换操作

`n` :跳过这个匹配的实例

`a` :对这个及随后所有匹配的字符串执行替换操作

`q or esc` :退出替换操作

`l` :执行这次替换并退出

`Ctrl-e, Ctrl-y` :分别是向下滚动和向上滚动

`vi file1 file2 file3...` :通过 vi，我们可以打开多个文件来编辑

`ls -l /usr/bin > ls-output.txt` :创建ls-output.txt这个文件

`vi foo.txt ls-output.txt` :用 vi 来编辑我们的原文件和新创建的文件

`ex` :文件之间切换

`:n` :从这个文件切换到下一个文件

`:N` :回到先前的文件

`:buffers` :显示文件列表

`:buffer 2` :切换到另一个(编号)

 打开另一个文件并编辑

`vi foo.txt` :打开foo.txt文件并编辑

`:e ls-output.txt` :加入ls-output.txt文件

当文件由：e 命令加载，你将无法用:n 或:N 命令来切换文件。这时要使用:buffer 命令加缓冲区号码，来切换文件

插入整个文件到另一个文件

`vi ls-output.txt` :打开ls-output.txt 并编辑

`:r foo.txt` ::r 命令（是 “read” 的简称）把指定的文件插入到光标位置之前

`:wq` :保存并退出

`:w foo1.txt` :也可以指定可选的文件名如果我们正在编辑 foo.txt 文件，想要保存一个副本，叫做 foo1.txt.

## 十三 自定制 shell 提示符

`ps1_old="$PS1"` :把已有的字符串复制到另一个 shell变量中

`PS1="$ps1_old"` :复原提示符

`PS1='\[\033[0;31m\]<\u@\h \W>\$'` :制作一个红色提示符

`PS1='\[\033[0;31m\]<\u@\h \W>\$\[\033[0m\]`' :终端仿真器恢复到原来的颜色

## 十四 软件包管理

`yum search emacs` :从yum资源库查找emacs文本编辑器

`apt-get update; apt-get install emacs` :从apt资源库安装emacs文本编辑器

`rpm -i emacs-22.1-7.fc7-i386.rpm` :(已经从一个并非资源库的网站下载了软件包文件 emacs-22.1-7.fc7-i386.rpm)通过软件包文件来安装软件

`yum erase package_name` :卸载 emacs 软件包

`apt-get update; apt-get upgrade` :经过软件库来更新软件包

`rpm -U emacs-22.1-7.fc7-i386.rpm` :经过软件包文件来升级软件

`rpm -qa` :列出所安装的软件包

`rpm -q package_name` :确定是否安装一个软件包

`yum info package_name` :显示所安装软件包的信息

`rpm -qf /usr/bin/vim` :查看哪个软件包安装了/usr/bin/vim 这个文件

## 十五章 存储媒介

`mount` :查看挂载的文件系统列表

`umount /dev/hdc` :卸载光盘(我们拥有 CD-ROM 光盘的设备名字)

`mkdir /mnt/cdrom` :创建一个新的光盘挂载点

`mount -t iso9660 /dev/hdc /mnt/cdrom` :把这个 CD-ROW 挂载到一个新的挂载点上。这个-t 选项用来指定文件系统类型

原因是我们不能卸载一个设备，如果某个用户或进程正在使用这个设备
的话。在这种情况下，我们把工作目录更改到了 CD-ROW 的挂载点，这个挂载点导致设备忙碌。我们可以很容易地修复这个问题通过把工作目录改到其它目录而不是这个挂载点

`ls /dev` :列出目录/dev（所有设备的住所）的内容

`/dev/fd*` :软盘驱动器

`/dev/hd*` :老系统中的 IDE(PATA) 磁盘

`/dev/lp*` :打印机

`/dev/sd*` :SCSI 磁盘

`/dev/sr*` :光盘（CD/DVD 读取器和烧写器）

`sudo tail -f /var/log/messages` :实时查看文件/var/log/messages （你可能需要超级用户权限）

`sudo fdisk /dev/sdb` : fdisk 命令操作分区

`m`按键 :显示程序菜单

`p`按键 :打印出这个设备的分区表

`t`按键 :更改分区id号

`w`按键 :保存

`q`按键 :不保存,退出

`mkfs` :命令创建一个新的文件系统

`sudo mkfs -t ext3 /dev/sdb1` :在此设备上创建一个 ext3 文件系统，我们使用 “-t” 选项来指定这个 “ext3” 系统类型，随后是我们要格式化的设备分区名称

`sudo mkfs -t vfat /dev/sdb1` :把这个设备重新格式化为它最初的 FAT32 文件系统，指定 “vfat” 作为文件系统类型

`sudo fsck /dev/sdb1` :检查文件系统的完整性之外，fsck 还能修复受损的文件系统

`sudo fdformat /dev/fd0` :格式化硬盘同时指定软盘设备名称（通常为/dev/fd0

`sudo mkfs -t msdos /dev/fd0` :通过 mkfs 命令，给这个软盘创建一个 FAT 文件系统

`dd if=/dev/sdb of=/dev/sdc` :把第一个驱动器中的所有数据复制到第二个驱动器中(有两个相同容量的 USB 闪存驱动器，并且要精确地把第一个驱动器（中的内容）复制给第二个。如果连接两个设备到计算机上)

`dd if=/dev/sdb of=flash_drive.img` :果只有第一个驱动器被连接到计算机上，我们可以把它的内容复制到一个普通文件中供以后恢复或复制数据

`dd if=/dev/cdrom of=ubuntu.iso` :制作一张现有 CD-ROM 的 iso 映像,拷贝到Ubuntu.iso

`genisoimage -o cd-rom.iso -R -J ~/cd-rom-files` :文件集合中创建一个映像(如果我们已经创建一个叫做 ∼/cd-rom-files 的目录，然后用文件填充此目录，再通过下面的命令来创建一个叫做 cd-rom.iso 映像文件)“-R” 选项添加元数据为 Rock Ridge 扩展，这允许使用长文件名和 POSIX 风格的文件权限。同样地，这个 “-J” 选项使 Joliet 扩展生效，这样 Windows 中就支持长文件名了

`mkdir /mnt/iso_image`
`mount -t iso9660 -o loop image.iso /mnt/iso_image` :添加 “-o loop” 选项来挂载（同时带有必需的 “-t iso9660” 文件系统类型），挂载这个映像文件就好像它是一台设备，把它连接到文件系统树上
我们创建了一个挂载点叫做/mnt/iso_image，然后把此映像文件image.iso挂载到挂载点上。映像文件被挂载之后，可以把它当作，就好像它是一张真正的 CD-ROM 或者 DVD

`wodim dev=/dev/cdrw blank=fast` :用 wodim 命令，指
定设备名称和清空的类型,清除一张可重写入的 CD-ROM(最小（且最快）的是 “fast” 类型)

`wodim dev=/dev/cdrw image.iso` :写入镜像(写入一个映像文件，我们再次使用 wodim 命令，指定光盘设备名称和映像文件名)

## 十六章 网络系统

`ping linuxcommand.org` :看看我们能否连接到网站 linuxcommand.org

`netstat -ie` :查看系统中的网络接口

`netstat -r`  :显示内核的网络路由表

`wget http://linuxcommand.org/index.php` :下载linuxcommand.org 网站的首页

`ssh itzou@192.168.200.129 free` :在名为 itzou@192.168.200.129 的远端主机上，执行 free 命令，并把输出结果显示到本地系统
shell 会话中

`ssh remote-sys 'ls \*' > dirlist.txt` :在远端系统中执行 ls 命令，并把命令输出重定向到本地系统中的一个文件里面

`ssh remote-sys 'ls * > dirlist.txt'` :把输出结果重定向到远端主机的文件中，我们可以把重定向操作符和文件名都放到单引号里面

`ssh -X itzou@192.168.200.129` :在名为 itzou@192.168.200.129 的远端系统中运行 xload 程序

`scp bob@remote-sys:document.txt .` :从 remote-sys 远端系统的家目录下复制文档 document.txt，到我们本地系统的当前工作目录下

`scp bob@remote-sys:document.txt .`

## 十七章 查找文件

`locate bin/zip` :locate 命令将会搜索它的路径名数据库，输出任一个包含字符串“bin/zip”的路径名

`locate zip | grep bin` :(输出包含字符串 zip) 然后查找 bin 的路径名并打印

`find ~` :输出我们的家目录的路径名列表

`find ~ | wc -l` :(输出我们的家目录的路径名列表)统计数量

`find ~ -type d | wc -l` :-type d 限制了只搜索目录

`find ~ -type f | wc -l` :限定搜索普通文件

`find ~ -type f -name "*.JPG" -size +1M | wc -l` :查找所有文件名匹配通配符模式“*.JPG”和文件大小大于 1M 的普通文件

`find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)` :查找家目录下文件权限不是0600或目录权限不是0700的(我们想要知道它是具有错误权限的文件还是有错误权限的目录。它不可能同时符合这两个条件)

`-and` :如果操作符两边的测试条件都是真，则匹配。可以简写为-a。注意若没有使用操作符，则默认使用 -and。

`-or` :若操作符两边的任一个测试条件为真，则匹配。可以简写为-o。

`-not` :若操作符后面的测试条件是假，则匹配。可以简写为一个感叹号（!）

`()` :把测试条件和操作符组合起来形成更大的表达式。这用来控制逻辑计算的优先级

`find ~ -type f -name '*.BAK' -delete` :删除扩展名为“.BAK”（这通常用来指定备份文件）的文件

`find ~ -type f -name '*.txt' -print` :命令会查找每个文件名以.txt (-name ‘*.txt’) 结尾的普通文件(-type f)，并把每个匹配文件的相对路径名输出到标准输出

`find ~ -type f -name 'foo*' -ok ls -l '{}' ';'` :搜索以字符串“foo”开头的文件名，并且对每个匹配的文件执行 ls-l 命令。(使用 -ok 行为来代替 -exec)使用 -ok 行为，会在 ls 命令执行之前提示用户

`find ~ -type f -name 'foo*' -exec ls -l '{}' +` :得到一样的结果，但是系统只需要执行一次 ls 命令

`find ~ -type f -name 'foo*' -print | xargs ls -l` :到 find 命令的输出被管道到 xargs 命令，之后，xargs 会为 ls 命令构建参数列表，然后执行 ls 命令

`mkdir -p playground/dir-{00{1..9},0{10..99},100}` :创建100个文件夹

`touch playground/dir-{00{1..9},0{10..99},100}/file-{A..Z}` :在每个文件夹中创建A-Z个文件

`find playground -type f -name 'file-A'` :找到在playground中名字带有file-A的文件

`find playground -type f -name 'file-A' | wc -l` :确认文件的数量

`touch playground/timestamp` :在playground下创建了一个空文件timestamp

`stat playground/timestamp` :会展示系统对timestamp及其属性所知道的所有信息

`find playground -type f -name 'file-B' -exec touch '{}' ';'` :更新操练场中所有名为 file-B 的文件

`touch playground/timestamp` :把它的修改时间设置为当前时间

`find playground -type f -name 'file-B' -exec touch '{}' ';'` :更新一些操练场中的文件

`find playground -type f -newer playground/timestamp` :通过把所有文件与参考文件 timestamp 做比较，来找到已更新的文件

## 第十八章 归档和备份

`gzip` :压缩或者展开文件

`gzip foo.txt` :压缩foo.txt文件

`gunzip foo.txt.gz` :解压foo.txt.gz文件

gzip 命令有许多选项
`-c` :把输出写入到标准输出，并且保留原始文件。也有可能用--stdout 和--to-stdout 选项来指定

`-d` :解压缩。正如 gunzip 命令一样。也可以用--decompress 或者--uncompress 选项来指定

`-f` :强制压缩，即使原始文件的压缩文件已经存在了，也要执行。也可以用--force 选项来指定

`-l` :列出每个被压缩文件的压缩数据。也可用--list 选项

`-h` :显示用法信息。也可用--help 选项来指定

`-r` :若命令的一个或多个参数是目录，则递归地压缩目录中的文件。也可用--recursive 选项来指定

`-t` :测试压缩文件的完整性。也可用--test 选项来指定

`-v` :显示压缩过程中的信息。也可用--verbose 选项来指定

`-number` :设置压缩指数。number 是一个在 1（最快，最小压缩）到
9（最慢，最大压缩）之间的整数。数值 1 和 9 也可以各自用--fast 和--best 选项来表示。默认值是整数 6

`ls -l /etc | gzip > foo.txt.gz` :创建了一个目录列表的压缩文件

`gunzip foo.txt.gz` :解压

`gunzip -c foo.txt.gz | less` :浏览一下压缩文本文件的内容

`ls -l /etc > foo.txt` :把etc 目录下的文件重定向到foo.txt中

`bzip2 foo.txt` :bzip2 程序使用起来和 gzip 程序一样

 `bunzip2 foo.txt.bz2` :bunzip2 和 bzcat 程序来解压缩文件。bzip2 文件也带有 bzip2recover 程序，其会试图恢复受损的.bz2 文件

`mkdir -p playground/dir-{00{1..9},0{10..99},100}`

`touch playground/dir-{00{1..9},0{10..99},100}/file-{A..Z}`

`tar cf playground.tar playground` :创建整个操练场的 tar 包(模式 c 和选项 f，其被用来指定这个 tar 包的名字)

`tar tf playground.tar` :列出归档文件的内容

`tar tvf playground.tar` :更详细的列表信息，我们可以添加选项 v

`mkdir foo`

`cd foo`

`tar xf ../playground.tar` :抽取 tar 包中的文件

`find playground -name 'file-A' -exec tar rf playground.tar '{}' '+'` :们使用 find 命令来匹配 playground 目录中所有名为 file-A 的文件，然后使用-exec行为，来唤醒带有追加模式（r）的 tar 命令，把匹配的文件添加到归档文件 playground.tar 里面

`find playground -name 'file-A' | tar czf playground.tgz -T -` :创建一个由 gzip 压缩的归档文件

`find playground -name 'file-A' | tar cjf playground.tbz -T -` :创建一个由 bzip2 压缩的归档文件

`mkdir remote-stuff`

`cd remote-stuff`

`ssh remote-sys 'tar cf - Documents' | tar xf -` :从远端系统 remote-sys 中复制目录 Documents 到本地系统名为 remote-stuff目录中

`zip -r playground.zip playground` :制作一个 playground 的 zip 版本的文件包(除非我们包含-r 选项，要不然只有 playground 目录（没有任何它的内容）被存储)

`zip -r playground.zip playground` :制作一个 playground 的 zip 版本的文件包

`cd foo`

`unzip ../playground.zip` :使用 unzip 程序，来直接抽取一个 zip 文件的内容

`find playground -name "file-A" | zip -@ file-A.zip` :使用 find 命令产生一系列与“file-A”相匹配的文件列表，并且把此列表管道到zip 命令，然后创建包含所选文件的文件包 file-A.zip

`ls -l /etc/ | zip ls-etc.zip -` :把 ls 命令的输出管道到 zip 命令。像 tar 命令，zip 命令把末尾的横杠解释为“使用标准输入作为输入文件。”

`unzip -p ls-etc.zip | less` :将解压缩的结果显示到屏幕上

`rsync options source destination` :rsync 被这样唤醒(这个程序能同步本地与远端的目录，通过使用
rsync 远端更新协议，此协议允许 rsync 快速地检测两个目录的差异，执行最小量的复制来达到目录间的同步。比起其它种类的复制程序，这就使 rsync 命令非常快速和高效。)

`rm -rf foo/*` :清空我们的 foo 目录

`rsync -av playground foo` :-a 选项（递归和保护文件属性）和-v 选项（冗余输出），来在 foo 目录中制作一个 playground 目录的镜像

`mkdir /media/BigDisk/backup` :创建一个目录，名为/backup

`sudo rsync -av --delete /etc /home /usr/local /media/BigDisk/backup` :我们把/etc，/home，和/usr/local 目录从我们的系统中复制到假想的存储设备中。我们包含了–delete 这个选项，来删除可能在备份设备中已经存在但却不再存在于源设备中的文件

`alias backup='sudo rsync -av --delete /etc /home /usr/local /media/BigDisk/backup'` :创建一个别名，并把它添加
到.bashrc 文件中

`sudo rsync -av --delete --rsh=ssh /etc /home /usr/local remote-sys:/backup` :我们添加了--rsh=ssh 选项，其
指示 rsync 使用 ssh 程序作为它的远程 shell。以这种方式，我们就能够使用一个 ssh 加密通道，把数据安全地传送到远程主机中。其次，通过在目标路径名前加上远端主机的名字（在这种情况下，远端主机名为 remote-sys），来指定远端主机

`mkdir fedora-devel`

`rsync -av -delete rsync://rsync.gtlib.gatech.edu/fedora-linuxcore/development/i386/os fedora-devel` :我们使用了远端 rsync 服务器的 URI，其由协议（rsync://），远端主机名（rsync.gtlib.gatech.edu），和软件仓库的路径名组成

## 第十九章 正则表达式

`ls /usr/bin | grep zip` :列出，位于目录 /usr/bin 中，文件名中包含子字符串“zip”的所有文件

`-i` :忽略大小写。不会区分大小写字符。也可用--ignore-case 来
指定。

`-v` :不匹配。通常，grep 程序会打印包含匹配项的文本行。这
个选项导致 grep 程序只会打印不包含匹配项的文本行

`-c` :打印匹配的数量（或者是不匹配的数目，若指定了-v 选项），
而不是文本行本身。也可用--count 选项来指定

`-l` :打印包含匹配项的文件名，而不是文本行本身，也可用--
files-with-matches 选项来指定

`-L` :相似于-l 选项，但是只是打印不包含匹配项的文件名。也可
用--files-without-match 来指定

`-n` :在每个匹配行之前打印出其位于文件中的相应行号。也可
用--line-number 选项来指定

`-h` :应用于多文件搜索，不输出文件名。也可用--no-filename 选
项来指定

创建一些文本文件来搜寻
`ls /bin > dirlist-bin.txt`

`ls /usr/bin > dirlist-usr-bin.txt`

`ls /sbin > dirlist-sbin.txt`

`ls /usr/sbin > dirlist-usr-sbin.txt`

`ls dirlist*.txt`

`grep bzip dirlist*.txt` :grep 程序在所有列出的文件中搜索字符串 bzip，然后找到两个匹配项，其都在文件 dirlist-bin.txt 中

`grep -l bzip dirlist*.txt` :如果我们只是对包含匹配项的文件列表，而不是对匹配项本身感兴趣的话，我们可以指定-l 选项

`grep -L bzip dirlist*.txt` :查看不包含匹配项的文件列表

`grep -h '.zip' dirlist*.txt` :查找包含正则表达式“.zip”的文本行
有几点需要注意一下。
注意没有找到这个 zip 程序。这是因为在我们的正则表达式中包含的圆点字符把所要求的匹配项的长度增加到四个字符，并且因为字符串“zip”只包含三个字符，所以这个 zip 程序不匹配。另外，如果我们的文件列表中有一些文件的扩展名是.zip，则它们也会成为匹配项，因为文件扩展名中的圆点符号也会被看作是“任意字符”

`grep -h '^zip' dirlist*.txt` :在正则表达式中，插入符号和美元符号被看作是锚点。这意味着正则表达式只有在文本行的开头或末尾被找到时，才算发生一次匹配

`grep -h 'zip$' dirlist*.txt`

`grep -h '^zip$' dirlist*.txt`

这里我们分别在文件列表中搜索行首、行尾以及行首和行尾同时包含字符串“zip”（例如，zip 独占一行）的匹配行。注意正则表达式‘ˆ$’（行首和行尾之间没有字符）会匹配空行

`grep -i '^..j.r$' /usr/share/dict/words` :“一个有五个字母的单词，它的第三个字母是‘j’，最后一个字母是‘r’

`grep -h '[bg]zip' dirlist*.txt` :们匹配包含字符串“bzip”或者“gzip”的任意行

`grep -h '[^bg]zip' dirlist*.txt` :激活否定操作，我们得到一个文件列表，它们的文件名都包含字符串“zip”，并且“zip”的前一个字符是除了“b”和“g”之外的任意字符

`grep -h '^[ABCDEFGHIJKLMNOPQRSTUVWXZY]' dirlist*.txt` :在列表中找到每个以大写字母开头的文件

`grep -h '^[A-Z]' dirlist*.txt`

`grep -h '^[A-Za-z0-9]' dirlist*.txt`

`grep -h '[A-Z]' dirlist*.txt` :匹配包含一个大写字母的文件名

`grep -h '[-AZ]' dirlist*.txt` :匹配包含一个连字符，或一个大写字母“A”，或一个大写字母“Z”的文件名

`grep -Eh '^(bz|gz|zip)' dirlist*.txt` :匹配以“bz”，或“gz”，或“zip”开头的文件名

`grep -Eh '^bz|gz|zip' dirlist*.txt` :匹配任意以“bz”开头，或包含“gz”，或包含“zip”的文件名

`echo "(555) 123-4567" | grep -E '^\(?[0-9][0-9][0-9]\)? [0-9][0-9][0-9]-[0-9]` :我们在圆括号之后加上一个问号，来表示它们将被匹配零次或一次。再一次，因为通常圆括号都是元字符（在 ERE 中），所以我们在圆括号之前加上了反斜杠，使它们成为文本字符(? 匹配零个或一个元素)

`echo "This works." | grep -E '[[:upper:]][[:upper:][:lower:] ]*\.'` :(*- 匹配零个或多个元素)这个表达式由三个元素组成：一个包含 [:upper:] 字符集的中括号表达式，一个包含 [:upper:]和 [:lower:] 两个字符集以及一个空格的中括号表达式，和一个被反斜杠字符转义过的圆点。第二个元素末尾带有一个* 元字符，所以在开头的大写字母之后，可能会跟随着任意数目的大写和小写字母和空格，并且匹配

`[:alnum:]` :字母数字字符。在 ASCII 中，等价于：[A-Za-z0-9]
`[:word:]` :与 [:alnum:] 相同, 但增加了下划线字符。
`[:alpha:]` :字母字符。在 ASCII 中，等价于：[A-Za-z]
`[:blank:]` :包含空格和 tab 字符。
`[:cntrl:]` :ASCII 的控制码。包含了 0 到 31，和 127 的 ASCII 字符。
`[:digit:]` :数字 0 到 9
`[:graph:]` :可视字符。在 ASCII 中，它包含 33 到 126 的字符。
`[:lower:]` :小写字母。
`[:punct:]` :标 点 符 号 字 符。 在 ASCII 中， 等 价 于：[-!”#$%&’()*+,./:;<=>?@[\\\]_‘|˜]
`[:print:]` :可打印的字符。在 [:graph:] 中的所有字符，再加上空格字符。
`[:space:]` :空白字符，包括空格、tab、回车、换行、vertical tab 和form feed. 在 ASCII 中，等价于：[ \t\r\n\v\f]
`[:upper:]` :大写字母。
`[:xdigit:]` :用来表示十六进制数字的字符。在 ASCII 中，等价于：[0-9A-Fa-f]

`echo "This that" | grep -E '^([[:alpha:]]+ ?)+$'` :(+  匹配一个或多个元素)

`echo "(555) 123-4567" | grep -E '^\(?[0-9]{3}\)? [0-9]{3}-[0-9]{4}$'` :({ } :匹配特定个数的元素)

`n` :匹配前面的元素，如果它确切地出现了 n 次。

`n,m` :匹配前面的元素，如果它至少出现了 n 次，但是不多于 m
次

`n,` :匹配前面的元素，如果它出现了 n 次或多于 n 次

`,m` :匹配前面的元素，如果它出现的次数不多于 m 次

`for i in {1..10}; do echo "($ {RANDOM: 0:3}) $ {RANDOM: 0:3}- $ {RANDOM:0:4}" >> phonelist.txt; done` :会创建一个包含 10 个电话号码的名为 phonelist.txt 的文件。每次重复这个命令的时候，另外 10 个号码会被添加到这个列表中

`cat phonelist.txt`

`grep -Ev '^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$' phonelist.txt` :查找无效的号码，并把搜索结果显示到屏幕上,使用-v 选项来产生相反的匹配，因此我们将只输出不匹配指定表达式的文本行

`find . -regex '.*[^-\_./0-9a-zA-Z].*'` :扫描发现包含空格和其他潜在不规范的路径名

`locate --regex 'bin/(bz|gz|zip)'` :搜索包含 bin/bz，bin/gz，或/bin/zip 字符串的路径名

less 和 vim 中查找文本
`less phonelist.txt`

`/([0-9]\{3\}) [0-9]\{3\}-[0-9]\{4\}`

## 第二十章 文本处理

`cat > foo.txt` : cat命令（随后指定了用于重定向输出的文件），然后输入我们的文本，最后按下 Enter 键来结束这一行，然后按下组合键 Ctrl-d，来指示 cat 程序

`cat -A foo.txt` :显示foo.txt的文本

`cat -ns foo.txt` :cat 程序也包含用来修改文本的选项。最著名的两个选项是-n，其给文本行添加行号和-s，禁止输出多个空白行

`sort > foo.txt` :sort 程序对标准输入的内容，或命令行中指定的一个或多个文件进行排序，然后把排序结果发送到标准输出。使用与 cat 命令相同的技巧

sort 程序有几个有趣的选项
`-b`  :默认情况下，对整行进行排序，从每行的第一个字符开始。这个选项导致 sort 程序忽略每行开头的空格，从第一个非空白字符开始排序

`-f`  :让排序不区分大小写

`-n`  :基于字符串的数值来排序。使用此选项允许根据数字值执行排序，而不是字母值

`-r`  :按相反顺序排序。结果按照降序排列，而不是升序

`-k` --key=field1[,field2] :对从 field1 到 field2 之间的字符排序，而不是整个文本行

`-m`  :把每个参数看作是一个预先排好序的文件。把多个文件合并成一个排好序的文件，而没有执行额外的排序

`-o`  :把排好序的输出结果发送到文件，而不是标准输出

`-t`  :定义域分隔字符。默认情况下，域由空格或制表符分隔

`du -s /usr/share/* | head` :du 命令列出的输出结果按照路径名来排序,把结果管道到 head 命令，把输出结果限制为前 10 行

`du -s /usr/share/* | sort -nr | head` :显示 10 个最大的空间消费者,使用此 -nr 选项，我们产生了一个反向的数值排序，最大数值排列在第一位

`ls -l /usr/bin | head`

`ls -l /usr/bin | sort -nr -k 5 | head` :让 sort 程序使用第五字段作为排序的关键值

`sort --key=1,1 --key=2n distros.txt` :我们指定了 1,1，意味着“始于并且结束于第一个字段。”在第二个实例中，我们指定了 2n，意味着第二个字段是排序的键值，并且按照数值排序。一个选项字母可能被包含在一个键值说明符的末尾，其用来指定排序的种类。这些选项字母和 sort 程序的全局选项一样：b（忽略开头的空格），n（数值排序），r（逆向排序）

`sort -k 3.7nbr -k 3.1nbr -k 3.4nbr distros.txt` :指定 -k 3.7，我们指示 sort 程序使用一个排序键值，其始于第三个字段中的第七个字符，对应于年的开头。同样地，我们指定 -k 3.1 和 -k 3.4 来分离日期中的月和日。我们也添加了 n 和 r 选项来实现一个逆向的数值排序。这个 b 选项用来删除日期字段中开头的空格（行与行之间的空格数迥异，因此会影响 sort 程序的输出结果

`sort -t ':' -k 7 /etc/passwd | head` :sort 程序提供了一个 -t 选项来定义分隔符。按照第七个字段（帐户的默认 shell）来排序此passwd 文件

`uniq` :uniq 会删除任意重复行，并且把结果发送到标准输出(常常和 sort 程序一块使用，来清理重复的输出)

`sort foo.txt | uniq` :先排序然后去重复

`-c` :输出所有的重复行，并且每行开头显示重复的次数

`-d` :只输出重复行，而不是特有的文本行

`-f n` :忽略每行开头的 n 个字段，字段之间由空格分隔，正如 sort
程序中的空格分隔符；然而，不同于 sort 程序，uniq 没有选项来设置备用的字段分隔符

`-i` :在比较文本行的时候忽略大小写

`-s n` :跳过（忽略）每行开头的 n 个字符

`-u` :只输出独有的文本行。这是默认的

`sort foo.txt | uniq -c` :uniq 被用来报告文本文件中重复行的次数，使用这个-c 选项

cut 程序被用来从文本行中抽取文本，并把其输出到标准输出

`-c` char_list :从文本行中抽取由 char_list 定义的文本。这个列表可能由一个或多个逗号分隔开的数值区间组成

`-f` field_list :从文本行中抽取一个或多个由 field_list 定义的字段。这个列表可能包括一个或多个字段，或由逗号分隔开的字段区间

`-d` delim_char :当指定-f 选项之后，使用 delim_char 做为字段分隔符。默认情况下，字段之间必须由单个 tab 字符分隔开

`--complement` :抽取整个文本行，除了那些由-c 和／或-f 选项指定的文本

`cat -A distros.txt` :使用带有 -A选项的 cat 命令，我们能查看是否这个文件符号由 tab 字符分离字段的要求

`cut -f 3 distros.txt` :使用 -f 选项来抽取一个字段

`cut -f 3 distros.txt | cut -c 7-10` :够抽取从位置 7 到 10 的字符

`cut -d ':' -f 1 /etc/passwd | head` :从/etc/passwd 文件中抽取第一个字段

`paste` :paste 命令的功能正好与 cut 相反。它会添加一个或多个文本列到文件中，而不是从文件中抽取文本列。它通过读取多个文件，然后把每个文件中的字段整合成单个文本流，输入到标准输出。类似于 cut 命令

`sort -k 3.7nbr -k 3.1nbr -k 3.4nbr distros.txt > distros-by-date.txt` :将产生一个按照日期排序的发行版列表，并把结果存储在一个叫做 distros-by-date.txt 的文件中

`cut -f 1,2 distros-by-date.txt > distros-versions.txt` :使用 cut 命令从文件中抽取前两个字段（发行版名字和版本号），并把结果存储到一个名为 distro-versions.txt 的文件中

`cut -f 3 distros-by-date.txt > distros-dates.txt`

`paste distros-dates.txt distros-versions.txt` :。通过使用 paste 命令，然后按照期望的顺序来安排它的参数，就能很容易完成这个任务
`join`:join 命令类似于 paste，它会往文件中添加列，但是它使用了独特的方法来完成。一个 join 操作通常与关系型数据库有关联，在关系型数据库中来自多个享有共同关键域的表格的数据结合起来，得到一个期望的结果。这个 join 程序执行相同的操作。它把来自于多个基于共享关键域的文件的数据结合起来

`cut -f 1,1 distros-by-date.txt > distros-names.txt`

`paste distros-dates.txt distros-names.txt > distros-key-names.txt`

`cut -f 2,2 distros-by-date.txt > distros-vernums.txt`

`paste distros-dates.txt distros-vernums.txt > distros-key-vernums.txt`

`join distros-key-names.txt distros-key-vernums.txt | head` :现在我们有两个具有共享键值（“发行日期”数据域）的文件。有必要指出，为了使 join 命
令能正常工作，所有文件必须按照关键数据域排序

`comm` :比较文本

`comm file1.txt file2.txt` :comm 命令产生了三列输出。第一列包含第一个文件独有的文本行；第二列，文本行是第二列独有的；第三列包含两个文件共有的文本行

`comm -12 file1.txt file2.txt` :只想输出两个文件共享的文本行，我们将隐藏第一列和第二列的输出结果

`diff` : diff 程序被用来监测文件之间的差异

`diff -c file1.txt file2.txt` :使用上下文模式（带上 -c 选项）

`diff -u file1.txt file2.txt` :统一模式相似于上下文模式，但是更加简洁。通过 -u 选项来指定它

`echo "lowercase letters" | tr a-z A-Z` :个 tr 程序被用来更改字符。我们可以把它看作是一种基于字符的查找和替换操作。换字是一种把字符从一个字母转换为另一个字母的过程,把小写字母转换成大写字母就是换字。我们可以通过 tr 命令来执行这样的转换

`echo "lowercase letters" | tr [:lower:] A` :把小写字母转换成A

`tr -d '\r' < dos_file > unix_file` :为了执行这个转换，每行末尾的回车符需要被删除。这个可以通过 tr 命令来执行这里的 dos_file 是需要被转换的文件，unix_file 是转换后的结果。这种形式的命令使用转义序列 \r 来代表回车符。

`echo "aaabbbccc" | tr -s ab` :tr 也可以完成另一个技巧。使用-s 选项，tr 命令能“挤压”（删除）重复的字符实例

`echo "front" | sed 's/front/back/'` :echo 命令产生了一个单词的文本流，然后把它管道给 sed 命令。sed，依次，对流文本执行指令 s/front/back/，随后输出“back”。我们也能够把这个命令认为是相似于 vi 中的“替换”（查找和替代）命令(sed 中的命令开始于单个字符。在上面的例子中，这个替换命令由字母 s 来代表，其后跟着查找和替代字符串，斜杠字符做为分隔符)

`echo "front" | sed 's_front_back_'` :通过紧跟命令之后使用下划线字符，则它变成界定符。sed 可以设置界定符的能力，使命令的可读性更强，正如我们将看到的

`echo "front" | sed '1s/front/back/'` :给我们的命令添加地址 1，就导致只对仅有一行文本的输入流的第一行执行替换操作

`n` :行号，n 是一个正整数

`$` :最后一行

`sed -n '1,5p' distros.txt` :我们打印出一系列的文本行，开始于第一行，直到第五行。为此，我们使用p 命令，其就是简单地把匹配的文本行打印出来。然而为了高效，我们必须包含选项 -n（不自动打印选项），让 sed 不要默认地打印每一行

`sed -n '/SUSE/p' distros.txt` :由斜杠界定的正则表达式 \/SUSE\/，我们能够孤立出包含它的文本行，和 grep程序的功能是相同的

`sed 's/\([0-9]\{2\}\)\/\([0-9]\{2\}\)\/\([0-9]\{4\}\)$/\3-\1-\2/' distros.txt`

`echo "aaabbbccc" | sed 's/b/B/'` :虽然执行了替换操作，但是只针对第一个字母“b”实例，然而剩余的实例没有更改。

`echo "aaabbbccc" | sed 's/b/B/g'` :通过添加 g 标志，我们能够更改所有的实例

`aspell` :能够智能地检查各种类型的文本文件，包括 HTML 文件，C/C++ 程序，电子邮件和其它种类的专业文本

`aspell check textfile` :textfile 是要检查的文件名

我们看到我们的文本中有一个拼写可疑且高亮显示的单词。在中间部分，
我们看到十个拼写建议，序号从 0 到 9，然后是一系列其它可能的操作。最后，在最底部，我们看到一个提示符，准备接受我们的选择。
如果我们按下 1 按键，aspell 会用单词“jumped”代替错误单词，然后移动到下一个拼写错的单词，就是“laxy”。如果我们选择替代物“lazy”，aspell 会替换“laxy”并且终止。一旦aspell 结束操作，我们可以检查我们的文件，会看到拼写错误的单词已经更正了

`sed -i 's/lazy/laxy/; s/jumped/jimped/' foo.txt` :还原拼写错误(这个 sed 选项-i，告诉 sed 在适当位置编辑文件，意思是不要把编辑结果发送到标准输出中。sed 会把更改应用到文件中，以此重新编写文件)

`aspell -H check foo.txt` :aspell 会认为 HTML 标志的内容是拼写错误。通过包含-H（HTML）检查模式选项，这个问题能够解决

## 第二十一章 格式化输出

`nl distros.txt | head` :添加文件的行数

nl 在计算文件行数的时候支持一个叫“逻辑页面”的概念。这允许 nl 在计算的时候去重设（再一次开始）可数的序列。用到那些选项的时候，可以设置一个特殊的开始值，并且在某个可限定的程度上还能设置它的式。一个逻辑页面被进一步分为 header(头),body(主体) 和 footer(尾部) 这样的元素

`-b` style :把 body 按被要求方式数行，可以是以下方式：a = 数所有行;t = 数非空行。这是默认设置。n = 无pregexp = 只数那些匹配了正则表达式的行

`-f` style :将 footer 按被要求设置数。默认是无

`-h` style :将 header 按被要求设置数。默认是

`-i` number :将页面增加量设置为数字。默认是一

`-n` format :设置数数的格式，格式可以是：ln = 左偏，没有前导零。rn = 右偏，没有前导零。rz = 右偏，有前导零。

`-p` :不要在没一个逻辑页面的开始重设页面数

`-s` string :在没一个行的末尾加字符作分割符号。默认是单个的 tab

`-v` number :将每一个逻辑页面的第一行设置成数字。默认是一

`-w` width :将行数的宽度设置，默认是六

`echo "The quick brown fox jumped over the lazy dog." | fold -w 12` :设定了行宽为 12 个字符。如果没有字符设置，默认是 80。注意到文本行不会因为单词边界而不会被分解

`echo "The quick brown fox jumped over the lazy dog."
| fold -w 12 -s` :增加的 -s 选项将让 fold 分解到最后可用的空白字符,即会考虑单词边界

`fmt` :一个简单的文本格式器

`fmt -w 50 fmt-info.txt | head` :重新格式这个文本并且让它成为一个 50 个字符宽的项目。我们能用 -w 选项对文件进行处理

`fmt -w 50 -p '# ' fmt-code.txt` :我们的示例文件包含了用“#”开始的注释（一个 # 后跟着一个空白符）和代码。现在，使用 fmt，我们能格式注释并且不让代码被触及(注意相邻的注释行被合并了，空行和非注释行被保留了)

`pr` :格式化打印文本

`pr -l 15 -w 65 distros.txt` :我们用 -l 选项（页长）和 -w 选项（页宽）定义了宽 65 列，长 15 行的一个“页面”

`printf "I formatted the string: %s\n" foo` :格式字符串可能包含文字文本（如“我格式化了这个字符串：”“I formatted the string:”），转义序列（例如\n，换行符）和以％字符开头的序列，这被称为转换规范。在上面的例子中，转换规范％s 用于格式化字符串“foo”并将其输出在命令行中

`d` :将数字格式化为带符号的十进制整数

`f` :格式化并输出浮点数

`o` :将整数格式化为八进制数

`s` :将字符串格式化

`x` :将整数格式化为十六进制数，必要时使用小写 a-f

`X` :与 x 相同，但变为大写

`%` :打印% 符号 (比如，指定“%%”)

`printf "%d, %f, %o, %s, %x, %X\n" 380 380 380 380 380 380` :380, 380.000000, 574, 380, 17c, 17C

`printf "%s\t%s\t%s\n" str1 str2 str3` :通过插入\t（tab 的转义序列），我们实现了所需的效果

`zcat /usr/share/man/man1/ls.1.gz | groff -mandoc >~/Desktop/foo.ps` :输出命令并将其存储到一个文件中,输出文件的图标应该出现在桌面上。双击图标，页面查看器将启动，并显示渲染后的文件

`ps2pdf ~/Desktop/foo.ps ~/Desktop/ls.pdf` :使用以下命令将 PostScript 输出的文件转换为 PDF（便携式文档格式）文件(ps2pdf 程序是 ghostscript 包的一部分，它安装在大多数支持打印的 Linux 系统上)

## 第二十二章 打印

`pr`  :转换需要打印的文本文件

`ls /usr/bin | pr -3 -w 65 | head` :道配合 pr 命令来做筛选。下面的例子中我们会列出目录 /usr/bin 并用 pr 将其格式化为 3 列输出的标题页

`ls /usr/bin | pr -3 | lpr` :打印多列目录列表

`lpstat -a` :查看系统已知打印机列表

显示了 lpr 的一些常用选项

`-# number` :设定打印份数为 number

`-p` :使每页页眉标题中带有日期、时间、工作名称和页码

`-P` :printer 指定输出打印机的名称。未指定则使用系统默认打印机

`-r` :打印后删除文件。对程序产生的临时打印文件较为有用

`ls /usr/bin | pr -4 -w 90 -l 88 | lp -o page-left=36 -o cpi=12 -o lpi=8` :打印我们的目录列表，这次我们设置 12 CPI、8 LPI 和一个半英寸的左边距

`ls /usr/bin | pr -3 -t | a2ps -o ~/Desktop/ls.ps -L 66` :用带 -t 参数（忽略页眉和页脚）的 pr 命令过滤数据流，然后用 a2ps 指定一个输出文件（-o 参数），并设定每页 66 行（-L 参数）来匹配 pr 的输出分页

`ls *.txt | pr -3 | lp` :打印以txt结尾的文件然后格式化3列打印

`lprm` 和 `cancel` :取消打印任务

`lpq` :显示打印机队列状态

`cancel 603` :终止并移除任务

## 第二十三章 编译程序

`which gcc` :查看编译器是否存在

`mkdir src`

`cd src`

`ftp ftp.gnu.org` :使用 ftp 协议把源码下载下来

因为我们是这个源码的“维护者”，当我们编译它的时候，我们把它保存在 ∼/src 目录下。由你的系统发行版源码会把源码安装在 /usr/src 目录下，而供多个用户使用的源码，通常安装在 /usr/local/src 目录下

`tar xzf diction-1.11.tar.gz` :一旦 tar 文件下载下来之后，必须解包。通过 tar 程序可以完成

`tar tzvf tarfile | head ---` :使用下面的命令，检查 tar 文件的内容

`less diction.c` :源码文件都是普通文本，可以用 less 命令查看

`make`  :只是构建需要构建的部分

`sudo make install` :安装程序

## 第二十四章 编写一个Shell脚本

`vi hello_world` :创建hello_world文本文件

`chmod 755 hello_world` :给文件设置权限为 755

`./hello_world` :执行脚本(加上./ 字符，来表明程序位于当前工作目录)

`echo $PATH` :这里我们看到了我们的目录列表。如果我们的脚本位于此列表中任意目录下，那么我们的问题将会被解决

`mkdir bin`

`mv hello_world bin`

`hello_world`

如果这个 PATH 变量不包含这个目录，我们能够轻松地添加它，通过在我们的.bashrc 文件中包含下面这一行文本：export PATH=~/bin:"$PATH"

`. .bashrc` :让 shell 重新读取这个.bashrc 文件

## 第二十五章 启动一个项目

`vim ~/bin/sys_info_page` :创建一个名为 ∼/bin/sys_info_page 的新文件

`chmod 755 ~/bin/sys_info_page` :修改权限为755

`filename="myfile"` :创建一个变量

`touch $filename` :确保他存在,没有就创建

`mv $filename ${filename}1` :把一个文件名从 myfile 改myfile1(通过添加花括号，shell 不再把末尾的 1 解释为变量名的一部分)

`df -h` :命令来确定磁盘空间的数量

`du -sh /home` :返回该目录的大小

## 第二十六章 流程控制语句: if 分支结构

当命令执行完毕后，命令（包括我们编写的脚本和 shell 函数）会给系统发送一个值，叫做退出状态。这个值是一个 0 到 255 之间的整数，说明命令执行成功或是失败。按照惯例，一个零值说明成功，其它所有值说明失败

`echo $?` :查看上一个命令的退出状态

文件表达式

`file1 -ef file2` :file1 和 file2 拥有相同的索引号（通过硬链接两个文件名指向相同的文件）

`file1 -nt file2` :file1 新于 file2

`file1 -ot file2` :file1 早于 file2

`-b file` :file 存在并且是一个块（设备）文件

`-c file` :file 存在并且是一个字符（设备）文件

`-d file` :file 存在并且是一个目录

`-e file` :file 存在

`-f file` :file 存在并且是一个普通文件

`-g file` :file 存在并且设置了组 ID

`-G file` :file 存在并且由有效组 ID 拥有

`-k file` :file 存在并且设置了它的“sticky bit”

`-L file` :file 存在并且是一个符号链接

`-O file` :file 存在并且由有效用户 ID 拥有

`-p file` :file 存在并且是一个命名管道

`-r file` :file 存在并且可读（有效用户有可读权限）

`-s file` :file 存在且其长度大于零

`-S file` :file 存在且是一个网络 socket

`-t fd` :fd 是一个定向到终端／从终端定向的文件描述符。这可以被用来决定是否重定向了标准输入／输出错误

`-u file` :file 存在并且设置了 setuid 位

`-w file` :file 存在并且可写（有效用户拥有可写权限）

`-x file` :file 存在并且可执行（有效用户有执行／搜索权限）

字符串表达式

`string` :string 不为 null

`-n string` :字符串 string 的长度大于零

`-z string` :字符串 string 的长度为零

`string1 = string2`
`string1 == string2`
string1 和 string2 相同。单或双等号都可以，不过双等号更受欢迎

`string1 != string2` :string1 和 string2 不相同

`string1 > string2` :sting1 排列在 string2 之后

`string1 < string2` :string1 排列在 string2 之前

整型表达式

`integer1 -eq integer2` :integer1 等于 integer2

`integer1 -ne integer2` :integer1 不等于 integer2

`integer1 -le integer2` :integer1 小于或等于 integer2

`integer1 -lt integer2` :integer1 小于 integer2

`integer1 -ge integer2` :integer1 大于或等于 integer2

`integer1 -gt integer2` :integer1 大于 integer2

(( )) 被用来执行算术真测试。如果算术计算的结果是非零值，则其测试值为真

&&（AND）和 ||（OR）操作符作用如同复合命令 [[ ]] 中的逻辑操作符

`command1 && command2`

`command1 || command2`

。对于 && 操作符，先执行 command1，如果并且只有如果 command1
执行成功后，才会执行 command2
对于 || 操作符，先执行command1，如果并且只有如果command1 执行失败后，才会执行 command2

`mkdir temp && cd temp`

`[ -d temp ] || mkdir temp` :会测试目录 temp 是否存在，并且只有测试失败之后，才会创建这个目录

## 第二十七章 读取键盘录入

`read` :从标准输入读取数值

read 支持以下选项:

`-a`  :把输入赋值到数组 array 中，从索引号零开始

`-d`  :用字符串 delimiter 中的第一个字符指示输入结束，而不是一个换行符

`-e` :使用 Readline 来处理输入。这使得与命令行相同的方式编辑输入

`-n` :读取 num 个输入字符，而不是整行

`-p` :为输入显示提示信息，使用字符串 prompt

`-r` :Raw mode. 不把反斜杠字符解释为转义字符

`-s` :Silent mode. 不会在屏幕上显示输入的字符。当输入密码和其它确认信息的时候，这会很有帮助

`-t` :超时. 几秒钟后终止输入。若输入超时，read 会返回一个非零退出状态

`-u` :使用文件描述符 fd 中的输入，而不是标准输入

`:syntax on` :使用带有语法高亮的编辑器将会帮助查找错误。如果安装了 vim 的完整版，通过输入下面的命令，可以使语法高亮生效

## 第二十八章 疑难排解

`cd $dir_name && rm *` : cd 命令执行成功之后，再运行 rm 命令

`[[ -d $dir_name ]] && cd $dir_name && rm *` :通过检验变量 dir_name 中包含的目录名是否真正地存在

bash 还提供了一种名为追踪的方法，这种方法可通过 -x 选项和 set 命令加上 -x 选项两种途径实现。拿我们之前的 trouble 脚本为例，给该脚本的第一行语句添加 -x 选项，我们就能追踪整个脚本。

们使用 set 命令加上 -x 选项来启动追踪，+x 选项关闭追踪。这种技术可以用来检查一个有错误的脚本的多个部分

until 是[条件]为假，则执行；while则是[条件]为真，则执行。

以下测试代码，只变化第4行，可观察执行结果的异同。-gt是大于的意思
