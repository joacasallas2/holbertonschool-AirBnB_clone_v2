-- Prepare a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
