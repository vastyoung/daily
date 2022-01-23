# mysql

## 安装mysql

我们只需以下几条命令就能安装mysql:

1. 修改我们软件仓库使用镜像站点源，修改为国内的镜像站点，这样我们下载软件更加的快速。

    ```test
    sudo pacman-mirrors -c China -i     #修改为国内的镜像站点

    pacman -Sy  #更新软件包的缓存
    ```

2. 使用我们的包管理器安装 mariadb(MariaDB 数据库管理系统是 MySQL 的一个分支)

    `sudo pacman -S mariadb`

3. 安装完成后会提示我们需要初始化 mariadb，然后我们通过以下命令即可完成初始化：

    `sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`
