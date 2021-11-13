
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
