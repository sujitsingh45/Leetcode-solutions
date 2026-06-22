# Write your MySQL query statement
DELETE p1
FROM Person p1
JOIN Person p2  # SELF JOINING
ON p1.email = p2.email
WHERE p1.id > p2.id; # delete whose id is greater