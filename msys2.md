# msys2

[MSYS2](https://www.msys2.org/)是一个在 Windows 平台上模拟 Linux 运行环境的一款软件，它还提供了一个名为 Pacman 的软件包管理系统，让我们更方便管理我们的软件包。

## 安装 msys2

1. 我们需要先下载 msys2 的安装程序 [msys2](https://github.com/msys2/msys2-installer/releases/download/2022-01-18/msys2-x86_64-20220118.exe)；

2. 我们运行安装程序。msys2 需要 64 位 Windows 7；

3. 选择我们想要安装 msys2 的路径；

4. 我们打开 msys2 ，第一次运行需要 更新包数据库和基础包：
`pacman -Syyu`

## 包管理器

msys2 软件发行版使用 pacman 来管理(安装、删除和更新)软件包。

寻找包的一些命令 ：

1. 寻找存储库中特定的包：

    ```test
    pacman -Ss <name or part of the name of the package>

    pacman -Ss openjp
    ```

2. 从已经安装的软件包中搜索:

    `pacman -Qs <name or part of the name of the package>`

3. 安装软件包:

    `pacman -S <name of the package>`

4. 卸载软件包 :
    `pacman -R <name of the package>`

5. 查找包的依赖项：
    `pactree mingw-w64-x86_64-gettext`

    `pacman -Qi mingw-w64-x86_64-gettext` #获取包的直接依赖项列表

6. 查找文件属于哪个包:
    `pacman -Qo <full file path>`

7. 列出包的内容
    `pacman -Ql <name of the package>`

    `pacman -Ql mingw-w64-x86_64-pugixml`

## 存储库和镜像

我们也是可以再 /etc/pacman.conf 配置文件中修改 镜像源的.

1. 我们先打开我们的终端模拟器；

2. 我们进入到 etc 目录

    `cd /etc/`

3. 使用文本编辑器打开 pacman.conf 配置文件
    `vi pacman.conf`

4. 按 i 进入输入模式,然后我们可以将以下配置粘贴到文件的末尾:

```test
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```

我们也可以看[Arch Linux CN Community repo mirrors list](https://github.com/archlinuxcn/mirrorlist-repo#arch-linux-cn-community-repo-mirrors-list)来选择我们喜欢的镜像源.

## 打包

### 构建包
