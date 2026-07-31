# Write your MySQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2  #self join
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1  # interval of day
WHERE w1.temperature > w2.temperature; #finding higher temperature

