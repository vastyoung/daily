# redis

## 安装rides

`sudo pacman -S redis` :使用 pacman 包管理器安装 rides

## 启动redis

`systemctl enable redis` :让 rides 开机自启

`systemctl start redis` :启动 rides

`redis-cli` :会让我进入这个终端(redis 127.0.0.1:6379>)

## redis 命令

在[菜鸟教程](https://www.runoob.com/)上面我们可以学到很多关于 redis 的命令.

[菜鸟教程 redis 命令](https://www.runoob.com/redis/redis-commands.html)

## redis 数据类型

redis 支持五种数据类型: string（字符串），hash（哈希），list（列表），set（集合）及zset(sorted set：有序集合)。

### string(字符串)

```test
redis 127.0.0.1:6379> SET runoob "菜鸟教程"
OK
redis 127.0.0.1:6379> GET runoob
"菜鸟教程"
```

### hash(哈希)

```test
redis 127.0.0.1:6379> DEL runoob #先删除前面 runoob 这个key
redis 127.0.0.1:6379> HMSET runoob field1 "Hello" field2 "World"
"OK"
redis 127.0.0.1:6379> HGET runoob field1
"Hello"
redis 127.0.0.1:6379> HGET runoob field2
"World"
```

### list(列表)

```test
redis 127.0.0.1:6379> DEL runoob
redis 127.0.0.1:6379> lpush runoob redis  # lpush 命令将一个或多个值插入到列表头部。 如果 key 不存在，一个空列表会被创建并执行 LPUSH 操作。
(integer) 1
redis 127.0.0.1:6379> lpush runoob mongodb
(integer) 2
redis 127.0.0.1:6379> lpush runoob rabbitmq
(integer) 3
redis 127.0.0.1:6379> lrange runoob 0 10    # lrange 返回列表中指定区间内的元素，区间以偏移量 START 和 END 指定。
1) "rabbitmq"
2) "mongodb"
3) "redis"
redis 127.0.0.1:6379>
```

### set(集合)

redis 的 set 是 string 类型的无序集合。

```test
redis 127.0.0.1:6379> DEL runoob
redis 127.0.0.1:6379> sadd runoob redis #添加一个 string 元素到 key 对应的 set 集合中，成功返回 1，如果元素已经在集合中返回 0。
(integer) 1
redis 127.0.0.1:6379> sadd runoob mongodb
(integer) 1
redis 127.0.0.1:6379> sadd runoob rabbitmq
(integer) 1
redis 127.0.0.1:6379> sadd runoob rabbitmq
(integer) 0
redis 127.0.0.1:6379> smembers runoob   #smembers 命令返回集合中的所有的成员

1) "redis"
2) "rabbitmq"
3) "mongodb"
```

### zset(sorted set：有序集合)

Redis zset 和 set 一样也是string类型元素的集合,且不允许重复的成员。

zadd 命令添加元素到集合，元素在集合中存在则更新对应score

`zadd key score member`

```test
redis 127.0.0.1:6379> DEL runoob
redis 127.0.0.1:6379> zadd runoob 0 redis
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 mongodb
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabbitmq
(integer) 1
redis 127.0.0.1:6379> zadd runoob 0 rabbitmq
(integer) 0
redis 127.0.0.1:6379> ZRANGEBYSCORE runoob 0 1000   #ZRANGEBYSCORE 返回有序集合中指定分数区间的成员列表。
1) "mongodb"
2) "rabbitmq"
3) "redis"
```
