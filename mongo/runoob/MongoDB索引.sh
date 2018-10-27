db.col.getIndexes();
db.col.ensureIndex({"title":1})
db.col.ensureIndex({"title":1, "description":-1})
db.col.ensureIndex({"title":1, "likes":-1},{"backgroud":true})
db.col.getIndexes();
db.col.dropIndex("title_1")
db.col.dropIndex("title_1_description_-1")
db.col.dropIndex("title_1_likes_-1")
db.col.getIndexes();