USE RUNOOB;

CREATE TABLE IF NOT EXISTS `runoob_tbl`(
	`id` int unsigned auto_increment,
	`title` varchar(100) NOT NULL,
	`author` varchar(40) NOT NULL,
	`create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (`id`)
) engine=InnoDB DEFAULT charset=utf8;
