-- name: get-entries-for-operation-by-sess_id
SELECT e.id,
       e.info,
       e.created_at,
       e.updated_at,
       (SELECT username FROM users WHERE id = e.author_id) as author_username
FROM entry e
         INNER JOIN operation a ON e.op_id = a.id ANd (a.sess_id = :sess_id);

-- name: get-entry-by-id^
SELECT e.id,
       e.info,
       e.created_at,
       e.updated_at,
       (SELECT username FROM users WHERE id = e.author_id) as author_username
FROM entry e
WHERE e.id = :entries_id;

-- name: create-new-entry<!
WITH users_subquery AS (
        (SELECT id, username FROM users WHERE username = :author_username)
)
INSERT
INTO entry (info, author_id, op_id)
VALUES (:info,
        (SELECT id FROM users_subquery),
        (SELECT id FROM operations WHERE sess_id = :sess_id))
RETURNING
    id,
    info,
        (SELECT username FROM users_subquery) AS author_username,
    created_at,
    updated_at;

-- name: delete-entry-by-id!
DELETE
FROM entry
WHERE id = :entry_id
  AND author_id = (SELECT id FROM users WHERE username = :author_username);
