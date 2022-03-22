DROP TABLE gyms;
DROP TABLE fittnes_classes;
DROP TABLE members;

CREATE TABLE fittnes_classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    fittnes_level VARCHAR (255),
    duration VARCHAR (255)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR (255),
    last_name VARCHAR (255),
    email_address VARCHAR (255),
    date_of_birth VARCHAR (255)
    
);

CREATE TABLE gyms (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fittnes_class_id INT REFERENCES fittnes_classes(id) ON DELETE CASCADE
);


