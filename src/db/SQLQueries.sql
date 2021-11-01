CREATE DATABASE cointracker;
USE cointracker;
CREATE TABLE Users (
id CHAR(32) PRIMARY KEY,
name VARCHAR(50) NOT NULL,
address VARCHAR(50) NOT NULL,
email VARCHAR(50));

INSERT INTO Users VALUES ("2afc86cab8b31f55b3747d6aedb5e12c","Souratendu","Seattle","souratendu@gmail.com");

CREATE TABLE Address (
address VARCHAR(50) PRIMARY KEY,
balance_usd DOUBLE NOT NULL,
spent_usd DOUBLE NOT NULL,
received_usd DOUBLE NOT NULL);

INSERT INTO Address VALUES("3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd", 1384.6146038400002, 332479.0276, 313864.3649);

CREATE TABLE User_Address (
id INT auto_increment,
userId CHAR(32) NOT NULL,
address VARCHAR(50) NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (userId) REFERENCES Users(id),
FOREIGN KEY (address) REFERENCES Address(address));

INSERT INTO User_Address VALUES(default, "2afc86cab8b31f55b3747d6aedb5e12c","3E8ociqZa9mZUSwGdSmAEMAoAxBK3FNDcd");