USE mysql;


SELECT *
FROM user
WHERE USER='zx'
  AND HOST='%';

 GRANT ALL PRIVILEGES ON *.* TO 'zx@%' identified BY 'zx_12221' WITH GRANT OPTION;


SELECT *
FROM user
WHERE USER='zx'
  AND HOST='%';