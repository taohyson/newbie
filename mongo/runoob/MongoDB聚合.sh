db.col.aggregate([{$group:{_id:"$by", num:{$sum:1}}}])
db.col.aggregate([{$project:{_id:1,by:1}}])
db.col.aggregate([{$match:{likes:{$gt:70,$lt:110}}}])