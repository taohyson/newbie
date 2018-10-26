USE RUNOOB;


DROP TABLE IF EXISTS `testalter_tbl`;


DROP TABLE IF EXISTS `alter_tbl`;


CREATE TABLE IF NOT EXISTS `testalter_tbl` (i INT, c CHAR(1));

 DESC testalter_tbl;


ALTER TABLE testalter_tbl
DROP i;

 DESC testalter_tbl;


ALTER TABLE testalter_tbl ADD i INT;

 DESC testalter_tbl;


ALTER TABLE testalter_tbl MODIFY i varchar(20);

 DESC testalter_tbl;


ALTER TABLE testalter_tbl change i j bigint;

 DESC testalter_tbl;

 SHOW TABLES;


ALTER TABLE testalter_tbl RENAME alter_tbl;

 SHOW TABLES;