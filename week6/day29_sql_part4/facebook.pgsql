-- postgres=# CREATE DATABASE facebook;
-- CREATE DATABASE
-- postgres=# \c facebook
-- You are now connected to database "facebook" as user "postgres".
-- facebook=# \i /home/buranidze/Documents/week6/day29_sql_part4/part42.sql

-- Напишите запрос,который выводит id из колонки пользователей и имя из колонки clients
facebook=# SELECT id, clients FROM part42;

-- Напишите запрос,который выводит всё о пользователе, чей логин содержит as, cg, si, am, qwe, er, ka, an
facebook=# SELECT * FROM part42 WHERE users LIKE '%as%' OR users LIKE '%cg%' Or users LIKE '%si%' OR users LIKE '%am%' OR users LIKE '%qwe%' OR users LIKE '%er%'OR users LIKE '%ka%' OR users LIKE '%an%';


-- Напишите запрос,который выводит всё о пользователе, чей логин заканчивается на lol, kan, ck, ie. ig
SELECT users FROM part42 WHERE RIGHT(users, 3) = 'lol' OR RIGHT(users, 3) = 'kan' OR RIGHT(users, 2) = 'ck' OR RIGHT(users, 2) = 'ie.'  OR RIGHT(users, 2) = 'ig';

-- Напишите запрос, который выводит всё о пользователе, чей логин начинается на a, b, c, d, M, D, A
SELECT users FROM part42 WHERE LEFT(users, 1) = 'a' OR LEFT(users, 1) = 'b' OR LEFT(users, 1) = 'c' OR LEFT(users, 1) = 'd'  OR LEFT(users, 1) = 'M' OR LEFT(users, 1) = 'D'  OR LEFT(users, 1) = 'A';

-- Как зовут самого знаменитого Сеньор Программиста(Senior Programmer) из Израиля(Israel)?
facebook=# SELECT first_name, country FROM part42 WHERE country='Israel' AND profession='Senior Editor';
 first_name | country 
------------+---------
 Waverley   | Israel
(1 row)

-- Выведите на экран всех пользователей у кого пустая почта
facebook=# SELECT *  FROM part42 WHERE email is NULL;

-- Посчитайте сколько пользователей у которых нет email живут на China.
facebook=# SELECT count(*) FROM part42 WHERE email IS NULL AND country = 'China'; 
 count 
-------
    70
(1 row)

-- Покажите имена и номера телефонов всех людей которые работают как Professor

facebook=# SELECT first_name, last_name, profession FROM part42
WHERE profession='Professor';
 first_name | last_name  | profession 
------------+------------+------------
 Sherilyn   | Ladewig    | Professor
 Conway     | Dobrowlski | Professor
 Aloysia    | Grimestone | Professor
 Teena      | Feldmesser | Professor
 Terri-jo   | Dark       | Professor
 Wayland    | Barkworth  | Professor
 Emmet      | MacCrosson | Professor
(7 rows)

-- У всех пользователей у которых почта ровняется False обновите почту на user@gmail.com
facebook=# UPDATE part42 SET email='user@gmail.com' WHERE email IS NULL;
UPDATE 393

-- Узнайте из каких стран люди которые имеюt работы(Professor).
facebook=# SELECT country,profession FROM part42 WHERE profession = 'Professor';
 country  | profession 
----------+------------
 China    | Professor
 Pakistan | Professor
 Poland   | Professor
 China    | Professor
 Russia   | Professor
 Russia   | Professor
 Poland   | Professor
(7 rows)


-- Везде где номер телефона начинается с 333 замените его любой РЕАЛЬНЫЙ номер в формате столбца phone_number.
facebook=# UPDATE part42 SET phone_number = '(111)88888888' WHERE phone_number LIKE '(333)%';


-- 12345, user123б, qwerty считается лёгкими паролями у каждого пользователя у кого лёгкий
-- пароль удалите из Базы Данных.
facebook=# DELETE FROM part42 WHERE password = 'rtdnW2' OR password = 'CP2iQqMirbwc' OR password = 'o1H2bHBA';
DELETE 3


-- Выведите на экран email всех .NET Developer разработчиков и отсортируйте их по Имени.
facebook=# SELECT first_name, email, profession FROM Part42 WHERE profession='Analyst Programmer' ORDER BY first_name;
 first_name |          email           |     profession     
------------+--------------------------+--------------------
 Burr       | bballachi7@exblog.jp     | Analyst Programmer
 Catlaina   | csnaddon5v@digg.com      | Analyst Programmer
 Hillary    | user@gmail.com           | Analyst Programmer
 Hortense   | hjosephilx@amazonaws.com | Analyst Programmer
 Mohandis   | mweatherhogg4n@usa.gov   | Analyst Programmer
 Shurlock   | user@gmail.com           | Analyst Programmer
(6 rows)


























