# Write your MySQL query statement below
SELECT uni.unique_id, emp.name
FROM Employees emp
LEFT OUTER JOIN EmployeeUNI uni
ON emp.id = uni.id;