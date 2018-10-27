use runoob;

# 'c'gd
db.createCollection("runoob");
show collections;

db.createCollection("mycol");
show collections;
db.mycol.insert({"name":"菜鸟教程"})
