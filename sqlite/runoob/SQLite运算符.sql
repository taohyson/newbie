.mode line
SELECT 10+20,
       10-20,
       10*20,
       10/5,
       12%5;

.mode column
SELECT *
FROM COMPANY
WHERE SALARY <> 20000;

.mode line
SELECT 60|13,
	   60&10,
	   (~60),
       (60>>2),
       (60<<2);