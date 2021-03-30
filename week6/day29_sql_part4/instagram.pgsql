-- postgres=# CREATE DATABASE instagram;
-- CREATE DATABASE

-- postgres=# \c instagram

-- instagram=# \i /home/buranidze/Documents/week6/day29_sql_part4/part4.sql

-- Посчитайте количество записей
instagram=# SELECT COUNT(*) FROM part4;

-- Сколько followerОВ у самого знаменитого пользователя
instagram=# SELECT MAX(followers) FROM part4;
  max   
--------
 998294
(1 row)

-- Напишите запрос, который выводит всю информацию самого знаменитого пользователя
instagram=# SELECT id, first_name,last_name,followers,users, country,email,profession FROM part4 ORDER BY followers desc limit 1;


 id  | first_name | last_name  | followers |     users     |  country  |         email          |   profession    
-----+------------+------------+-----------+---------------+-----------+------------------------+-----------------
 923 | Pascale    | Greensides |    998294 | pgreensidespm | Indonesia | pgreensidespm@ebay.com | Cost Accountant


-- Найдите среднее количество подписчиков

instagram=# SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY followers) FROM part4;
 percentile_cont 
-----------------
          523016

-- Отсортируйте всех пользователей по логину
instagram=# SELECT users FROM part4;

-- Отсортируйте всех пользователей по стране
instagram=# SELECT users, country FROM part4;

-- Отсортируйте всех пользователей по email
instagram=# SELECT users, email FROM part4;










