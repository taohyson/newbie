USE mysql;


SELECT HOST,
       USER,
       password,
       select_priv,
       insert_priv,
       update_priv
FROM user;


INSERT INTO user(HOST,
                 USER,
                 password,
                 select_priv,
                 insert_priv,
                 update_priv)
VALUES ('%',
        'zx',
        'zx_12221',
        'Y',
        'Y',
        'Y');


SELECT HOST,
       USER,
       password,
       select_priv,
       insert_priv,
       update_priv
FROM user;