-- Last updated: 10/2/2026, 10:11:09 AM
# Write your MySQL query statement below
select tweet_id  from tweets
where length(content) > 15;