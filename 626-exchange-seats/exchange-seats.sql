# Write your MySQL query statement below
SELECT
    IF(id % 2 = 0,
       id - 1,
       IF(id = (SELECT COUNT(*) FROM Seat), id, id + 1)  #if the current id is odd then swap by next
    ) AS id,
    student
FROM Seat
ORDER BY id;