# 在 windows 上使用 vmworkstation 安装 linux 虚拟机

我们的个人电脑使用的操作系统通常都是 windows，如果要体验 linux 操作系统，一般有以下几种做法：

1. 在个人电脑上重新装一个 linux 系统以替换 windows 系统；
2. 将个人电脑安装成双系统，让 linux 系统和 windows 系统共存；
3. 在 windows 系统中使用虚拟机软件安装体验 linux 系统；

使用第三种方式在 windows 系统中使用虚拟机软件不会影响我们本来的系统，让我们一台电脑也能体验不同的操作系统，就算虚拟机坏掉了，也不会影响我们本来的系统，只用重新安装一个虚拟机就可以了。

## 1. windows 上常见的虚拟机软件有哪些?

windows 上常见的虚拟机软件有这些:

1. [VMware Workstation](https://www.vmware.com/cn/products/workstation-pro.html) ：VMware Workstation 是一款容易安装和使用，对新手友好且免费的软件。

2. [VirtualBox](https://www.virtualbox.org/) ：VirtualBox 是一款流行的入门级虚拟机软件，并且它是开源，完全免费的；

3. [VMware Fusion](https://www.vmware.com/products/fusion.html) ：VMware Fusion 是一款为 mac 用户提供的虚拟机软件，该软件页面精美，功能强大。

## vmworkstation 是哪家公司的软件? 这个软件有什么特点?

[vmworkstation](https://www.vmware.com/cn/products/workstation-pro.html) 是 [VMware](https://www.vmware.com/hk.html) 公司的所开发的软件。该软件的特点主要有以下几点：

1. vmworkstation  该软件能在一台电脑上同时运行多个虚拟机，并且虚拟机和宿主机之间相互独立。

2.

3.

## 什么是 "linux 发行版"? "发行版"的概念是什么?

linux 发行版是以Linux内核为中心，集成各种各样的系统管理软件或应用工具软件从而形成一套完整的操作系统，这种操作系统被称为linux发行版.

## 如何查看/知道有哪些linux发行版可用?

我通常在[DistroWatch](https://distrowatch.com/)这个网站上面查看 linux发行版,这个网站上面包含了各种 linux 发行版的信息，人气排名。

## 如何查看对应发行版的官网?

在[DistroWatch](https://distrowatch.com/)我们可以网站中点击我们想要查看的 Linux 发行版，会有关于对应的 linux 发行版的信息，信息中会对于发行版的官网。

## 如何获取特定linux发行版的系统安装镜像?

我们可以先进入[DistroWatch](https://distrowatch.com/)这个网站，然后点击我们想要的 linux 发行版，里面有关于这个发行版相关的信息，然后我们点击信息中的主页，进入这个发行版的官网，最后点击下载即可。

## linux 发行版的官方软件仓库的概念是什么?

linux 发行版的官方软件仓库是一个为用户而建的软件仓库，用户可以在软件仓库维护和分享新的软件包。

## 软件仓库的镜像站是什么概念?

软件仓库的镜像站是将网站的多个副本发置到不同的服务器上面,例如我们想下载一个国外的软件的包，我们用国外的镜像来下载是比较慢的，我们可以国内的镜像站，这样提高了我们的下载软件的速度。

## 有哪些著名的镜像站?

我所知道著名的镜像站有这些：

1. [中国科学技术大学开源软件镜像](https://mirrors.ustc.edu.cn/)

2. [清华大学开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/)

3. [阿里云开源镜像站](https://developer.aliyun.com/mirror/)

## 镜像站里可以找到官方提供的linux 发行版系统安装镜像吗?(尝试一下)

## 如何使用 vmworkstation 安装系统镜像?附带截图说明

## 软件仓库包管理器是什么概念?

[软件仓库包管理器](https://wiki.archlinux.org/title/Pacman_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))可以帮助我们简化对软件包的管理，让我们通过包管理器就能安装软件仓库中需要软件，也能通过包管理器对软件包进行更新和删除操作。

## 如何配置软件仓库使用镜像站点源?

我们可以通过这几步配置我们软件仓库使用的镜像站点：

1. 我们先打开我们的终端模拟器；

2. 我们进入到 etc 目录

    `cd /etc/`

3. 使用文本编辑器打开 pacman.conf 配置文件
    `vim pacman.conf`

4. 按 i 进入输入模式,然后我们可以将以下配置粘贴到文件的末尾:

```test
[archlinuxcn]
Server = https://repo.archlinuxcn.org/$arch
```

我们也可以看[Arch Linux CN Community repo mirrors list](https://github.com/archlinuxcn/mirrorlist-repo#arch-linux-cn-community-repo-mirrors-list)来选择我们喜欢的镜像源.

## 使用包管理器安装拼音输入法?
