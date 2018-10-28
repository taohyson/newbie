.mode column
.header on

INSERT INTO company
VALUES(7,
       'John',
       'navinfo',
       33,
       20000);


SELECT *
FROM company;


DELETE
FROM company
WHERE id = 7;


SELECT * FROM company;