USE RUNOOB;


DROP TABLE IF EXISTS `person_tbl`;


CREATE TABLE IF NOT EXISTS `person_tbl`(`name` varchar(255)) engine=InnoDB DEFAULT charset=utf8;


INSERT INTO person_tbl
VALUES('start'), ('ok'), ('start ok'), ('today is march'), ('are you'), ('look at me'), ('look');


SELECT name
FROM person_tbl
WHERE name REGEXP '^st';


SELECT name
FROM person_tbl
WHERE name REGEXP 'ok$';


SELECT name
FROM person_tbl
WHERE name REGEXP 'mar';


SELECT name
FROM person_tbl
WHERE name REGEXP '^[aeiou]|ok$';