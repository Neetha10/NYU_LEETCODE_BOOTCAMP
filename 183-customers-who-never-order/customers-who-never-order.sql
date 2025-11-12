# Write your MySQL query statement below
select c.name Customers
from Customers c
LEFT JOIN orders o
on c.Id=o.customerId
where o.CustomerId is NULL;