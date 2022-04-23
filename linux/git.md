# git

## git 命令

`git status` :查看 git 当前状态

`git log` :查看当前分支提交历史记录

`git log test` :查看 test 分支的提交记录

`git diff` :查看当前工作区所做的修改

`git diff test` :将当前分支的内容和 本地仓库的 test 分支的内容进行对比

`git diff origin/test` :将当前分支的内容和 origin 远端的test分支的内容进行对比

`git checkout  +分支名` :将已经存在的指定分支切出到工作区

`git checkout -b +分支名` :新建分支

`git branch` : 查看所有分支，以及当前所在分支。

`git add` :添加当前工作区所做的修改到暂存区

`git commit -m "描述"` :提交暂存区的内容到本地仓库

`git push origin master` :将本地仓库推到远端仓库

`git pull origin master` :从远端仓库拉取 master 分支的内容并合并到本地的当前分支

`git fetch origin` :拉取远端最新更改(但并不合并到当前分支)

`git clone +仓库链接` :克隆一个已存在的仓库

`git remote -v` :列出当前已配置的远端仓库

`git stash` :将工作区的修改的内容暂存的垃圾桶

`git stash pop` :将垃圾桶中的内容弹出到工作区

`git reset HEAD~n` :将本分支的前 n 个提交的修改撤销到工作区

`git rebase test` :变基 将当前分支的起源点平移到指定点(test)

## 终端命令

```sh
#设置终端中的网络代理环境
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
export all_proxy="socks5://127.0.0.1:7890"
```
