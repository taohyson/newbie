 USE RUNOOB;


DROP TABLE `runoob_test_tbl`;


CREATE TABLE IF NOT EXISTS `runoob_test_tbl` (runoob_author varchar(40) NOT NULL, runoob_count INT) engine=InnoDB DEFAULT charset=utf8;


INSERT INTO runoob_test_tbl (runoob_author, runoob_count)
VALUES ('RUNOOB',
        20);


INSERT INTO runoob_test_tbl (runoob_author, runoob_count)
VALUES ('菜鸟教程',
        NULL);


INSERT INTO runoob_test_tbl (runoob_author, runoob_count)
VALUES ('Google',
        NULL);


INSERT INTO runoob_test_tbl (runoob_author, runoob_count)
VALUES ('FK',
        20);


SELECT *
FROM runoob_test_tbl;


-- SELECT *
-- FROM runoob_test_tbl
-- WHERE runoob_count = NULL;


-- SELECT *
-- FROM runoob_test_tbl
-- WHERE runoob_count != NULL;


SELECT *
FROM runoob_test_tbl
WHERE runoob_count IS NULL;


SELECT *
FROM runoob_test_tbl
WHERE runoob_count IS NOT NULL;

