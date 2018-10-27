# foreach in (Z)-add/range/rem/rank/card/rangebylex/rangebyscore
del runoobkey
Zadd runoobkey 1 redis
Zadd runoobkey 2 mongo
Zadd runoobkey 3 mysql
Zadd runoobkey 4 mysql
Zrange runoobkey 0 10 withscores
Zcard runoobkey
Zrank runoobkey mysql
Zrem runoobkey mongo
Zrank runoobkey mysql

del runoobkey