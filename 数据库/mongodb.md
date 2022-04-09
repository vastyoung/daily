# mongodb

`\mongodb\bin\mongod --dbpath e:\data\db` : 运行MongoDB 服务器

`\mongodb\bin\mongo.exe` :连接MongoDB

## linux

`systemctl status mongodb` :查看 mongodb 服务状态

`systemctl enable mongodb` :设置 mongodb 开机自启

`systemctl status mongodb`

`systemctl start  mongodb` :启动 mongodb 服务

`systemctl status mongodb`

`ip -4 a` :查看 iPv4 地址

`sudo vim /etc/mongodb.conf` :把 ipv4 地址添加到 mongodb.conf 文件

`systemctl restart mongodb` 重启 mongodb 服务
