USE photochnaja_db;

CREATE TABLE users
(
    id         INTEGER      NOT NULL IDENTITY(1,1),
    login      VARCHAR(32)  NOT NULL,
    password   CHAR(80)     NOT NULL,
    email      VARCHAR(64)  NOT NULL,
    CONSTRAINT USERS_ID_PK PRIMARY KEY (id),
    CONSTRAINT USERS_LOGIN_UQ UNIQUE (login),
    CONSTRAINT USERS_EMAIL_UQ UNIQUE (email),
);