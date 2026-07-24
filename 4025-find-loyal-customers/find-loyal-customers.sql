# Write your MySQL query statement below
SELECT
    customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING
    #At least 3 purchase transactions
    SUM(transaction_type = 'purchase') >= 3

    #Active for at least 30 days
    AND DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30

     #Refund rate < 20%
    AND SUM(transaction_type = 'refund') / COUNT(*) < 0.2

ORDER BY customer_id;