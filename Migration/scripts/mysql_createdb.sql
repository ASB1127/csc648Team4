USE  topicmatchdb;
CREATE TABLE Profile (
    id INT PRIMARY KEY,
    firstname VARCHAR(255) NOT NULL,
    lastname  VARCHAR(255) NOT NULL
);

INSERT INTO Profile (id,firstname,lastname) VALUES(0,"Amit","Bal");
