# Write your MySQL query statement below
UPDATE Salary
SET sex =
    CASE  #swapping the sex
        WHEN sex = 'm' THEN 'f'
        ELSE 'm'
    END;
