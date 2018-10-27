#if'u'r
db.col.find();
db.col.update({"title":"MongoDB 教程"}, {"$set":{"title":"MongoDB"}})
db.col.find();
db.col.save({
    "_id" : ObjectId("5bd3d0f983bd343c05667f3b"),
    "title" : "MongoDB",
    "description" : "MongoDB 是一个 Nosql 数据库",
    "by" : "Runoob",
    "url" : "http://www.runoob.com",
    "tags" : [
            "mongodb",
            "NoSQL"
    ],
    "likes" : 110
})
db.col.find()
db.col.save({
    "title" : "MongoDB",
    "description" : "MongoDB 是一个 Nosql 数据库",
    "by" : "Runoob",
    "url" : "http://www.runoob.com",
    "tags" : [
            "mongodb",
            "NoSQL"
    ],
    "likes" : 110
})
db.col.find()