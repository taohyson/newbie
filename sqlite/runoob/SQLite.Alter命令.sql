.table
CREATE TABLE IF NOT EXISTS company_new(id int);

.table
ALTER TABLE company_new RENAME TO company_old;

.table
ALTER TABLE company_old ADD COLUMN sex char(1);

.schema company_old
DROP TABLE company_old;