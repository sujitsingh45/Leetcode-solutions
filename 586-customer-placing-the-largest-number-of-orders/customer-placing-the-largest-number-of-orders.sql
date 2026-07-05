# Write your MySQL query statement below
SELECT customer_number
FROM Orders
GROUP BY customer_number #grouping to get the count of order
ORDER BY COUNT(*) DESC #making it in descending order
LIMIT 1; #printing only one who has more order