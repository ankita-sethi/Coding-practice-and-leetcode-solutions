--1378. Replace Employee ID With The Unique Identifier

select u.unique_id, e.name from employeeuni u right join employees e
on u.id=e.id
