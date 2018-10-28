CREATE INDEX IF NOT EXISTS salary_index ON COMPANY(salary);

.header on
.mode column
SELECT * FROM COMPANY INDEXED BY salary_index WHERE salary > 5000;