-- 1378. Replace Employee ID With The Unique Identifier
SELECT EmployeeUNI.unique_id, Employees.name
FROM EmployeeUNI 
RIGHT JOIN Employees ON EmployeeUNI.id = Employees.id;