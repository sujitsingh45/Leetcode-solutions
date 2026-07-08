# Write your MySQL query statement below
SELECT MAX(num) AS num
FROM MyNumbers #selecting maximum form those count one
WHERE num IN (  
    # selecting single count number
    SELECT max(num)
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
);


