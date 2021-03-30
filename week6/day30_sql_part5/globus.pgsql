-- postgres=# CREATE DATABASE globus;
-- CREATE DATABASE
-- postgres=# \c globus
-- You are now connected to database "globus" as user "postgres".
-- globus=# \i /home/buranidze/Documents/week6/day30_sql_part5/globus5.sql

-- Найдите сколько разных типов продуктов в таблице globus.
globus=# SELECT COUNT (DISTINCT product_type) FROM globus5;
 count 
-------
   381
(1 row)

-- Используя HAVING найдите сколько и каких продуктов в narodnii испортятся меньшечем через 2 дня.
