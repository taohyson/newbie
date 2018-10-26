USE RUNOOB;

 SHOW
CREATE TABLE runoob_tbl \G;

 SHOW tables;


DROP TABLE IF EXISTS `runoob_tbl_copy`;

-- LIKE's COPY 
CREATE TABLE IF NOT EXISTS `runoob_tbl_copy` LIKE runoob_tbl;


INSERT INTO runoob_tbl_copy
SELECT *
FROM runoob_tbl;


SELECT *
FROM runoob_tbl_copy;


DROP TABLE IF EXISTS `runoob_tbl_copy`;

-- SELECT's COPY
CREATE TABLE IF NOT EXISTS `runoob_tbl_copy`
SELECT *
FROM runoob_tbl;


SELECT *
FROM runoob_tbl_copy;


DROP TABLE `runoob_tbl_copy`;