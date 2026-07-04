# Write your MySQL query statement below
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = #conditon that all product key should be there 
(
    SELECT COUNT(*)
    FROM Product
);