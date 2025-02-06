# Write your MySQL query statement below
SELECT mng.employee_id, mng.name, COUNT(emp.reports_to) AS reports_count, ROUND(AVG(emp.age)) as average_age
FROM Employees mng
INNER JOIN Employees emp
WHERE mng.employee_id = emp.reports_to
GROUP BY mng.employee_id
ORDER BY mng.employee_id;