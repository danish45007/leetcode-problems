# Write your MySQL query statement below
select email as Email from (select email,count(email) as ce from person group by email) as temp
where temp.ce > 1
