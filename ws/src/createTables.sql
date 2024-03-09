CREATE DATABASE IF NOT EXISTS TopicMatch;
USE TopicMatch;

grant all on *.* to 'root'@'%' with grant option;
FLUSH PRIVILEGES;

CREATE TABLE Users (
    
    PersonID int NOT NULL AUTO_INCREMENT,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255),
    PRIMARY KEY (PersonID)
);

CREATE TABLE Message (
    mID int NOT NULL AUTO_INCREMENT,
    toUser int,
    fromUser int,
    msg varchar(255),
    PRIMARY KEY (mID),
    FOREIGN KEY (toUser)
        REFERENCES Users(PersonID),
    FOREIGN KEY (fromUser)
        REFERENCES Users(PersonID)
       
);


INSERT INTO Users (PersonID, LastName, FirstName, City) VALUES(1,'Bal','Amit','San Jose');

