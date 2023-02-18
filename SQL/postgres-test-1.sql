CREATE TYPE status AS ENUM('Cancelled', 'Finished', 'InProgress');
CREATE TABLE trips(
   TRIP_ID SERIAL PRIMARY KEY,
   CUST_ID INTEGER REFERENCES users(USER_ID),
   DRIVER_ID INTEGER REFERENCES users(USER_ID),
   STATUS            status default 'InProgress',
   TRIP_VALUE        FLOAT,
   TRIP_DATE         DATE
);
ALTER TABLE trips 
ADD CONTSTRAINT fk_cust_id
FOREIGN KEY (CUST_ID) 
REFERENCES users (USER_ID);

ALTER TABLE trips 
ADD CONTSTRAINT fk_driver_id
FOREIGN KEY (DRIVER_ID) 
REFERENCES users (USER_ID);

INSERT INTO
   trips (cust_id, driver_id, status, trip_value, trip_date)
VALUES
   (1,4,'Finished','')

DROP TYPE status;
ALTER TABLE trips DROP CONSTRAINT FK_CUST_ID;
ALTER TABLE trips DROP CONSTRAINT FK_DRIVER_ID;
DROP TABLE trips;









CREATE TYPE banned AS ENUM('Yes','No');
CREATE TABLE users(
   USER_ID SERIAL PRIMARY KEY,
   NAME        CHAR(255),
   BANNED            banned default 'No'
);

INSERT INTO users (name) VALUES ('Andy'), ('John'), ('Larry'), ('Brian'), ('Michelle'), ('Charlie'), ('Harley')
INSERT INTO users (name, banned) VALUES ('Oscar', 'Yes'), ('Terry', 'Yes'), ('Kevin', 'Yes')

DROP TYPE banned;
DROP TABLE users;











