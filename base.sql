CREATE TABLE users (
    name   TEXT (1, 16) NOT NULL,
    userID INTEGER      PRIMARY KEY
                        UNIQUE
                        NOT NULL,
    passw               NOT NULL,
);
INSERT INTO users (name, userID, passw) VALUES (SwwarmGost, 00000000, 12345678)