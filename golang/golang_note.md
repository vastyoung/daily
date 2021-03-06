
# `golang笔记:`

`sudo pacman -Syy` :强制更新

## Archlinux pacman

`pacman -Si` :浏览已安装软件的可选依赖

`pacman -S package_name1 package_name2 ...` :安装或者升级单个软件包或者一系列软件包

`pacman -S $(pacman -Ssq package_regex)` :正则表达式安装多个软件包

`pacman -S extra/package_name` :有时候在不同的软件仓库中，一个软件包有多个版本（比如[extra]和[testing]）。可以选择一个来安装

`pacman -S gnome` :一些包属于一个可以同时安装的软件包组会提醒用户选择 gnome 内需要安装的包

`Enter a selection (default=all): 1-10 15` :pacman 还支持选择或排除某个区间内的的软件包(这将选中序号 1 至 10 和 15 的软件包)

`Enter a selection (default=all): ^5-8 ^2` :会选中除了序号 5 至 8 和 2 之外的所有软件包

`pacman -Sg gnome` :查看哪些包属于 gnome 组

`pacman -R package_name` :删除单个软件包，保留其全部已经安装的依赖关系

`pacman -Rs package_name` :删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系

`pacman -Rsu package_name` :上面这条命令在移除包含其他所需包的组时有时候会拒绝运行。这种情况下可以尝试

`pacman -Rsc package_name` :删除软件包和所有依赖这个软件包的程序(此操作是递归的，请小心检查，可能会一次删除大量的软件包)

`pacman -Rdd package_name` :删除一个被其他软件包依赖的软件包，但是不删除依赖这个软件包的其他软件包

`pacman -Rn package_name` :pacman 删除某些程序时会备份重要配置文件，在其后面加上*.pacsave扩展名。-n 选项可以避免备份这些文件

`pacman -Syu` :升级整个系统

`pacman -Ss string1 string2 ...` :在包数据库中查询软件包，查询位置包含了软件包的名字和描述

`pacman -Ss '^vim-'` :有时，-s的内置正则会匹配很多不需要的结果，所以应当指定仅搜索包名，而非描述或其他子段

`pacman -Qs string1 string2 ...` :要查询已安装的软件包

`pacman -F string1 string2 ...` :按文件名查找软件库

`pacman -Si package_name` :显示软件包的详尽的信息

`pacman -Qi package_name` :查询本地安装包的详细信息

`pacman -Ql package_name` :要获取已安装软件包所包含文件的列表

`pacman -Fl package_name` :查询远程库中软件包包含的文件

`pacman -Qk package_name` :检查软件包安装的文件是否都存在

`pacman -Qo /path/to/file_name` :询数据库获取某个文件属于哪个软件包

`pacman -F /path/to/file_name` :查询文件属于远程数据库中的哪个软件包

`pacman -Qdt` :罗列所有不再作为依赖的软件包

`pacman -Qet` :罗列所有明确安装而且不被其它包依赖的软件包

`pactree package_name` :显示软件包的依赖树

`paccache -r` :默认会删除所有缓存的版本和已卸载的软件包，除了最近的3个会被保留

`paccache -rk1` :设置保留最近几个版本

`pacman -Sc` :删除目前没有安装的所有缓存的包，和没有被使用的同步数据库

`paccache -ruk0` :添加-u/--uninstalled开关来限制paccache的行为只作用于卸载的包。例如清理所有卸载的包的缓存版本

`pacman -Sc` :删除目前没有安装的所有缓存的包，和没有被使用的同步数据库

`pacman -Scc` :删除缓存中的全部文件，使用两次-c开关。这是最为激进的方式，将会清空缓存文件夹

`pacman -Syu package_name1 package_name2 ...` :升级系统时安装其他软件包

`pacman -Sw package_name` :下载包而不安装它

`pacman -U /path/to/package/package_name-version.pkg.tar.zst` :安装一个本地包,不从源里下载

`pacman -U file:///path/to/package/package_name-version.pkg.tar.zst` :将本地包保存至缓存

`pacman -U http://www.example.com/repo/example.pkg.tar.zst` :安装一个远程包（不在 pacman 配置的源里面）

`pacman -S --asdeps package_name` :当安装软件包时，可以把安装原因强制设为依赖

`pacman -D --asdeps package_name` :改变某个已安装软件包的安装原因

`pacman -Fy` :同步文件数据库

`pacman -F pacmany` :查询一个包含具体文件的包名

pacman 的配置文件位于/etc/pacman.conf

升级前对比版本

要查看旧版和新版的有效安装包，请取消/etc/pacman.conf中"VerbosePkgLists"的注释。修改后的 `pacman -Syu`

`NoUpgrade=path/to/file` :升级时跳过文件

`NoExtract=usr/lib/systemd/system/*` :总是跳过某些文件夹的安装，可以将它们放到 NoExtract 中，例如不想安装 systemd 模块

`Include = /path/to/common/settings` :如果你有多个配置文件（比如，主配置和启用了测试仓库的配置文件），需要共享一些设置，你可以在配置文件中使用Include选项

"Failed to commit transaction (invalid or corrupted package)" 错误
看看/var/cache/pacman/pkg中是否有*.part结尾的文件，它们是没有完全下载的文件，删除它们并重新执行更新。这些程序一般是自定义的XferCommand 下载命令造成的

`find /var/cache/pacman/pkg/ -iname "*.part" -delete`

`find-iname"MyProgram.c"` :查找指定的文件名不区分大小写

"Failed to init transaction (unable to lock database)" 错误
pacman 在改变软件包数据库前，比如安装软件包时，会创建一个文件锁 /var/lib/pacman/db.lck。这会阻止其他 pacman 实例在同一时间修改软件包数据库
如果 pacman 在更新数据库时被打断，旧锁可能保留下来。如果确认没有 pacman 实例在运行，那么删掉文件锁

`rm /var/lib/pacman/db.lck`

`pacman -Q $(pactree -u pacman)` :查看依赖项的完整列表

## List of applications

`command | curl -F c=@- https://ptpb.pw` :使用curl访问ptpb.pw, sprunge.us 和 ix.io 的pastebins. 比如把一个命令的管道输出到ptpb

`curl -F c=@- https://ptpb.pw < file` :传一个文件 (包括图片)

## 第一章入门

Go 是编译型的语言.通过 go 命令配合其子命令进行使用.最简单的子命令是 run,它将一个或多个以.go为后缀的源文件进行编译,链接然后运行生成可执行文件

`go run helloworld.go` :Helloworld

`go build helloworld.go` :编译输出一个可复用的程序

`./helloworld`

fmt 包中的函数用来格式化输出和扫描输入,Println 是 fmt 中的一个基本的输出函数.
我们先告诉辨编译器源文件需要那些,用 Package 声明后面的 import 来导入这些包.

os 包提供了一些函数和变量,命令行参数以 os 包中 Args名字的变量供程序访问,在 os 包外以 os.Args 这个名字
变量 os.Args 是一个字符串 slice 他是用动态容量的数组 s,可以通过 s[i] 来访问单个元素,通过 s[s:n]来访问一段连续子区间,数组长度用 len(s) 表示
os.Args的第一个元素是 os.Args[0]

`sep + os.Args[i]` :将 sep 和 os.Args[i] 追加到一起

`s += sep + os.Args[i]` :将 sep 和 os.Args 追加到旧 s 上面,并重新赋值给 s,等价于 s = s + sep + os.Args[i]

condition 是一个布尔表达式,在循环的每一次迭代开始前推演,如果推演结果是真,循环则继续

//传统的 while 循环
for condition {
    //...
}

//传统的无限循环
for {
    //...
}

循环可以通过 break 或 return 等语句终止

每一次迭代 range 产生一对值 :索引和这个索引出元素的值

声明字符串变量的方式
s := ""
var s = ""
