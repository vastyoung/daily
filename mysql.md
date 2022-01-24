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

## 命令

`SHOW DATABASES;` : 列出数据库列表

`use RUNOOB;` ： use 命令接数据库名称(选择要操作的数据库)

`SHOW TABLES;` : 查看该数据库下有哪些表

`SHOW COLUMNS FROM runoob_tbl;`:  显示runoob_tbl表的属性

`exit` : 退出mysql 命令提示窗口

`CREATE DATABASE 数据库名;` : 创建数据库

`drop database RUNOOB;` : 删除名为 RUNOOB 的数据库

`CREATE TABLE table_name (column_name column_type);` :创建数据表

```sql
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

`DROP TABLE table_name ;` : 删除数据表

```sql
#表中插入数据
INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN );
```

`select * from runoob_tbl;` : 读取数据表

```sql
#如果所有的列都要添加数据可以不规定列进行添加数据
mysql> INSERT INTO runoob_tbl
    -> VALUES
    -> (0, "JAVA 教程", "RUNOOB.COM", '2016-05-06');
```

```sql
#查询数据
SELECT column_name,column_name  
FROM table_name                 #可以查询多个表表之间用逗号分隔
[WHERE Clause]                  #使用WHERE语句来设定查询条件
[LIMIT N][ OFFSET M]            #使用 LIMIT 属性来设定返回的记录数
```
