USE RUNOOB;

 -- insert into runoob_tbl (title, author) values('学习 Python','RUNOOB.COM'),('学习 C','FK');

CREATE TABLE IF NOT EXISTS `tcount_tbl`(`id` int auto_increment, `author` varchar(40), `count` int, PRIMARY KEY (`id`)) engine=InnoDB DEFAULT charset=utf8;

 -- insert into tcount_tbl (author, count) values ('菜鸟教程','10'),('RUNOOB.COM','20'),('Google','22');

SELECT *
FROM runoob_tbl;


SELECT *
FROM tcount_tbl;


SELECT a.id,
       a.author,
       b.count
FROM runoob_tbl a,
     tcount_tbl b
WHERE a.author = b.author;


SELECT a.id,
       a.author,
       b.count
FROM runoob_tbl a
INNER JOIN tcount_tbl b
ON a.author = b.author;


SELECT a.id,
       a.author,
       b.count
FROM runoob_tbl a
LEFT JOIN tcount_tbl b
ON a.author = b.author;


SELECT a.id,
       a.author,
       b.count
FROM runoob_tbl a
RIGHT JOIN tcount_tbl b
ON a.author = b.author;