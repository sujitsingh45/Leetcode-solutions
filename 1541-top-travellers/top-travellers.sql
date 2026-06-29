# Write your MySQL query statement below
SELECT
    u.name,
    COALESCE(SUM(r.distance), 0) AS travelled_distance #null converted to zero
FROM Users u
LEFT JOIN Rides r
    ON u.id = r.user_id
GROUP BY u.id, u.name  #grouping on id and user_id
ORDER BY travelled_distance DESC, u.name ASC; #condition

