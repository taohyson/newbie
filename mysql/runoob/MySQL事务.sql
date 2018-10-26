USE RUNOOB;


DROP TABLE IF EXISTS `runoob_transaction_test`;


CREATE TABLE IF NOT EXISTS `runoob_transaction_test`(id int(5)) engine=innodb;

 -- 创建数据表

SELECT *
FROM runoob_transaction_test;

 -- 开始事务
BEGIN;


INSERT INTO runoob_transaction_test value(5);


INSERT INTO runoob_transaction_test value(6);

 -- 提交事务
COMMIT;


SELECT *
FROM runoob_transaction_test;

 -- 开始事务
BEGIN;


INSERT INTO runoob_transaction_test
VALUES(7);

 -- 回滚
ROLLBACK;

 -- 因为回滚所以数据没有插入

SELECT *
FROM runoob_transaction_test;