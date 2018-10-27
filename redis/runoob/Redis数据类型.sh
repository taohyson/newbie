SET name "runoob"
get name

hmset myhash field1 'Hello' field2 'world'
hget myhash field1
hget myhash field2

lpush mylist redis
lpush mylist mongo
lpush mylist rabitmq
lrange mylist 0 10

sadd myset redis
sadd myset mongo
sadd myset rabitmq
sadd myset rabitmq
smembers myset

zadd myzet 0 redis
zadd myzet 0 mongo
zadd myzet 0 rabitmq
zadd myzet 0 rabitmq
zrangebyscore myzet 0 1000