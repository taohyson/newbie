SELECT *
FROM sqlite_sequence;


DELETE
FROM sqlite_sequence
WHERE name = 'table_name';


UPDATE sqlite_sequence
SET seq = 0
WHERE name = 'table_name';