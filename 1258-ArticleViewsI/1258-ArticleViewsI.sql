-- Last updated: 10/2/2026, 10:11:11 AM
# Write your MySQL query statement below
select distinct author_id  as id from views
where  author_id = viewer_id
order by id