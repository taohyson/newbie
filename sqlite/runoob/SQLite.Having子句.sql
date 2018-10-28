.mode column
.header on

SELECT *
FROM company
GROUP BY salary HAVING age=min(age)
ORDER BY id;