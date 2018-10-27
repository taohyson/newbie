# *-set/get/del/incr
SET runoobkey redis
get runoobkey
getset runoobkey redis-server
getrange runoobkey 1 8

SETEX runoobkey 10 redis-cli
setnx runoobkey hi
get runoobkey
setrange runoobkey 6 bench
get runoobkey
strlen runoobkey
del runoobkey

set runoobkey 5
incr runoobkey
decrby runoobkey 2
del runoobkey