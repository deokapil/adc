-- name: get-entries-for-operation-by-sess_id
SELECT e.id,
       e.info,
       a.sess_id,
       e.created_at,
       e.updated_at
FROM entry e
         INNER JOIN operation a ON e.op_id = a.id ANd (a.sess_id = :sess_id);

-- name: get-entry-by-id^
SELECT e.id,
       e.info,
       a.sess_id,
       e.retval,
       e.created_at,
       e.updated_at
FROM entry e
    INNER JOIN operation a ON e.op_id = a.id;
    WHERE e.id = :entries_id;

-- name: create-new-entry<!
INSERT
INTO entry (info, op_id, retval)
VALUES (:info,
        (SELECT id FROM operation WHERE sess_id = :sess_id),
        :retval)
RETURNING
    id,
    info,
    :sess_id as sess_id,
    retval,
    created_at,
    updated_at;

-- name: delete-entry-by-id!
DELETE
FROM entry
WHERE id = :entry_id;
