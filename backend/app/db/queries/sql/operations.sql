-- name: get-operation-by-session^
SELECT id,
       sess_id,
       created_at,
       updated_at,
       (SELECT username FROM users WHERE id = author_id) AS author_username
FROM operation
WHERE sess_id = :sess_id
LIMIT 1;


-- name: create-new-operation<!
WITH author_subquery AS (
    SELECT id, username
    FROM users
    WHERE username = :author_username
)
INSERT
INTO operation (sess_id, author_id)
VALUES (:sess_id, (SELECT id FROM author_subquery))
RETURNING
    id,
    sess_id,
        (SELECT username FROM author_subquery) as author_username,
    created_at,
    updated_at;


-- name: delete-operation!
DELETE
FROM operation
WHERE sess_id = :sess_id
  AND author_id = (SELECT id FROM users WHERE username = :author_username);
