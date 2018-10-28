.header on
.mode column

CREATE INDEX salary_index ON COMPANY (salary);
SELECT * FROM sqlite_master WHERE type = 'index';
DROP INDEX salary_index;