-- name: get-user-by-name^
SELECT id,
       username,
       name,
       salt,
       hashed_password,
       created_at,
       updated_at
FROM users
WHERE name = :name
LIMIT 1;


-- name: get-user-by-username^
SELECT id,
       username,
       name,
       salt,
       hashed_password,
       created_at,
       updated_at
FROM users
WHERE username = :username
LIMIT 1;


-- name: create-new-user<!
INSERT INTO users (username, name, salt, hashed_password)
VALUES (:username, :name, :salt, :hashed_password)
RETURNING
    id, created_at, updated_at;


-- name: update-user-by-username<!
UPDATE
    users
SET username        = :new_username,
    name            = :new_name,
    salt            = :new_salt,
    hashed_password = :new_password,
WHERE username = :username
RETURNING
    updated_at;
