# foreach in (Z)-add/range/rem/card/rank/rangebylex/rangebyscore
del runoobkey
Zadd runoobkey 1 redis
Zadd runoobkey 2 mongo
Zadd runoobkey 3 mysql
Zadd runoobkey 4 mysql
Zrange runoobkey 0 10 withscores

del runoobkey