CREATE DATABASE IF NOT EXISTS easy_access;
USE easy_access;

CREATE TABLE IF NOT EXISTS users (
  `user_id` int(50) NOT NULL AUTO_INCREMENT,
  `device_number` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS scripts (
  `script_id` int(50) NOT NULL AUTO_INCREMENT,
  `script_name` varchar(50) NOT NULL,
  `user_id` int(50) NOT NULL,
  `content` varchar(2000) NOT NULL,
  `date_created` date NOT NULL,
  PRIMARY KEY (`script_id`),
  FOREIGN KEY (`user_id`)
    REFERENCES users (`user_id`)
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS websockets (
  `connection_id` varchar(50) NOT NULL,
  `user_id` varchar(50) NOT NULL,
  `connection_status` varchar(50) NOT NULL,
  `connection_time` date NOT NULL,
  `ip_address` varchar(255) NOT NULL,
  `endpoint` varchar(50) NOT NULL,
  PRIMARY KEY (`connection_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `users` (`user_id`, `device_number`, `password`)
  VALUES (1, 'user1', 'hellopass')
  ON DUPLICATE KEY UPDATE `user_id`=`user_id`;
