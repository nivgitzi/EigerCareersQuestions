SELECT department.NAME as 'DepartmentName', COUNT(employee.ID) as 'AmountOfEmployees'
FROM employee
RIGHT JOIN department
ON Employee.DEPT_ID = department.ID
GROUP BY department.NAME
ORDER BY COUNT(employee.ID) DESC, department.NAME ASC;