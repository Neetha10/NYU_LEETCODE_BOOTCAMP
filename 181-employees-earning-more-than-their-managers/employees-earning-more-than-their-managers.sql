# Write your MySQL query statement below
select e.name AS Employee
FROM Employee e
LEFT JOIN Employee m
ON e.ManagerId= m.id
Where e.salary > m.salary;


