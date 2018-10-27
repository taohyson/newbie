# foreach in {H}-set/get/del/keys/vals/getall/exists/len
Hmset runoobkey name "runoob tutorial" description "redis basic commands for caching" likes 20 visitors 23000
Hgetall runoobkey
Hlen runoobkey
Hkeys runoobkey
Hvals runoobkey

Hincrby runoobkey visitors 1
Hdel runoobkey visitors
Hexists runoobkey visitors
Hget runoobkey visitors

del runoobkey