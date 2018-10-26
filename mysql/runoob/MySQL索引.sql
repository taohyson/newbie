USE RUNOOB;


DROP TABLE IF EXISTS `zxtable`;

 -- 创建表的时候直接指定

CREATE TABLE zxtable(ID INT NOT NULL, username VARCHAR(16) NOT NULL, INDEX zxindex0 (username(16)));

 SHOW INDEX
FROM zxtable;


CREATE INDEX zxindex1 ON zxtable(username(16));


ALTER TABLE zxtable ADD INDEX zxindex2(username(16));

 SHOW INDEX
FROM zxtable;


CREATE UNIQUE INDEX zxindex3 ON zxtable(username(16));


ALTER TABLE zxtable ADD UNIQUE zxindex4(username(16));

 SHOW INDEX
FROM zxtable;


DROP INDEX zxindex0 ON zxtable;

 SHOW INDEX
FROM zxtable;


ALTER TABLE zxtable
DROP INDEX zxindex1;


ALTER TABLE zxtable
DROP INDEX zxindex2;

 SHOW INDEX
FROM zxtable;


ALTER TABLE zxtable
DROP INDEX zxindex3;


ALTER TABLE zxtable
DROP INDEX zxindex4;

 SHOW INDEX
FROM zxtable;