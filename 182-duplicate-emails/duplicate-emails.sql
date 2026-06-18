# Write your MySQL query statement below
SELECT email AS Email #renames the output column to match the required format.
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;  #keeps only those emails that occur more than once.