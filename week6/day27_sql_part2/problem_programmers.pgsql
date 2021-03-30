-- Создайте БД programmers.
postgres=# CREATE DATABASE programmers;
CREATE DATABASE
postgres=# 

-- Добавьте таблицу students:
-- id - Уникальный номер записи.
-- name - Имя студента
-- age - Возраст студента
-- fp_language - Основной Язык программирования
-- sp_language - Второй Язык программирования

programmers=# CREATE TABLE students(
id SERIAL PRIMARY KEY,
name VARCHAR,
age INT,
fp_language VARCHAR,
sp_language VARCHAR);
CREATE TABLE
programmers=#

-- В таблицу students, добавить записи:
-- id| name  | age| fp_language | sp_language
-- 1 | Bakyt | 23 | Python      | С++
-- 2 | Aygul | 46 | Python      | Java
-- 3 | Jika  | 13 | C           | Ruby_On_Rails
-- 4 | Ermek | 16 | Java        | C
-- 5 | Artem | 55 | C#          | Java
-- 6 | Roma  | 31 | Pascal      | C
-- 7 | Beka  | 25 | C#          | JavaScript

programmers=# SELECT * FROM students;


-- Напишите запрос, который выводит все имена студентов и языки программирования.
programmers=# SELECT name, fp_language, sp_language FROM students;


-- Напишите запрос, который выводит возраст студентов которым больше 30.
programmers=# SELECT name, age FROM students WHERE age > 30;


-- Выведите на экран всех студентов которые знают только Python или C#.

programmers=# SELECT name, fp_language, sp_language FROM students WHERE fp_language = 'Python' OR fp_language = 'C#' OR sp_language = 'C#' OR sp_language='Python';


-- Выведите на экран всех студентов которые знают Python и C# или C# и Java.

programmers=# SELECT name, fp_language, sp_language FROM students WHERE fp_language = 'Python' AND sp_language = 'C#' OR fp_language = 'C#' AND sp_language='Java';


-- Удалите всех студентов id которых равен 1, 3, 5, 7.
programmers=# DELETE FROM students WHERE id='1' OR id='3' OR id='5' OR id='7';
DELETE 3
programmers=# SELECT * FROM students;


-- Узнайте самого молодого студента который знает Java.
programmers=# SELECT * FROM students WHERE age= (SELECT MIN(age) FROM students)



-- Удалите таблицу students.
programmers=# DROP TABLE students;

-- Удалите БД programmers.
programmers=# DROP DATABASE programmers;




