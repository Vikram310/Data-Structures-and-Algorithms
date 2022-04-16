# Write your MySQL query statement below

UPDATE Salary
SET sex = (case when sex = 'm'
          then 'f'
          else 'm'
          END)