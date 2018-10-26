USE RUNOOB;


DROP TABLE `Websites`;


CREATE TABLE IF NOT EXISTS `Websites`(`id` int NOT NULL auto_increment, `name` varchar(40) NOT NULL, `url` varchar(255) NOT NULL, `alexa` int NOT NULL, `country` varchar(255) NOT NULL, PRIMARY KEY (`id`)) engine=InnoDB DEFAULT charset=utf8;


DROP TABLE `apps`;


CREATE TABLE IF NOT EXISTS `apps`(`id` int NOT NULL auto_increment, `app_name` varchar(40) NOT NULL, `url` varchar(255) NOT NULL, `country` varchar(255) NOT NULL, PRIMARY KEY (`id`)) engine=InnoDB DEFAULT charset=utf8;


INSERT INTO `Websites` (name, url, alexa, country)
VALUES ("Google",
        "https://www.google.cm/",
        1,
        "USA"), ("淘宝",
                 "https://www.taobao.com/",
                 13,
                 "CN"), ("菜鸟教程",
                         "http://www.runoob.com/",
                         4689,
                         "CN"), ("微博",
                                 "http://weibo.com/",
                                 20,
                                 "CN"), ("Facebook",
                                         "https://www.facebook.com/",
                                         3,
                                         "USA"), ("stackoverflow",
                                                  "http://stackoverflow.com/",
                                                  0,
                                                  "IND");


INSERT INTO apps(app_name, url, country)
VALUES ("QQAPP",
        "http://im.qq.com/",
        "CN"), ("微博APP",
                "http://weibo.com/",
                "CN"), ("淘宝APP",
                        "https://www.taobao.com/",
                        "CN");


SELECT *
FROM Websites;


SELECT *
FROM apps;


SELECT country
FROM Websites
UNION
SELECT country
FROM apps;


SELECT country
FROM Websites
UNION ALL
SELECT country
FROM apps;


SELECT country,
       name
FROM Websites
WHERE country = 'CN'
UNION ALL
SELECT country,
       app_name
FROM apps
WHERE country = 'CN'
ORDER BY country;