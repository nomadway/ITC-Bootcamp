
-- Создайте БД department
postgres=# CREATE DATABASE department;
CREATE DATABASE

-- Создайте таблицу developers(id,name,skill,programming_lang по умолчанию установите
-- значение HTML):
postgres=# CREATE TABLE developers(
postgres(# id SERIAL PRIMARY KEY,
postgres(# name VARCHAR,
postgres(# skill VARCHAR,
postgres(# programming_lang VARCHAR DEFAULT 'HTML');
CREATE TABLE

-- Переименуйте колонку skill на age.
department=# ALTER TABLE developers RENAME COLUMN skill TO age;
ALTER TABLE
department=# SELECT * FROM developers;
 id | name | age | programming_lang 
----+------+-----+------------------
(0 rows)

ALTER TABLE developers ALTER COLUMN age TYPE INTEGER USING(trim(age)::integer);

-- В таблицу developers, добавить запись:
-- 5. Добавить 'Bakyt', 23, 'Python'
-- 6. Добавить Beka, 15 лет Java
-- 7. Добавьте Gulya, 30 лет, JavaScript
-- 8. Добавьте Beka, 39 лет, Assembler

department=# \d developers
department=# INSERT INTO developers(
department(# name,
department(# age,
department(# programming_lang)
department-# VALUES(
department(# 'Bakyt',
department(# 23,
department(# 'Python');
INSERT 0 1
department=# INSERT INTO developers(
name,
age,
programming_lang)
VALUES(
'Beka',
15,
'Java');
INSERT 0 1
department=# INSERT INTO developers(
name,
age,
programming_lang)
VALUES(
'Gulya',
30,
'JavaScript');
INSERT 0 1
department=# INSERT INTO developers(
name,
age,
programming_lang)
VALUES(
'Beka',
39,
'Assembler');
INSERT 0 1

department=# SELECT * FROM developers;
 id | name  | age | programming_lang 
----+-------+-----+------------------
  1 | Bakyt |  23 | Python
  2 | Beka  |  15 | Java
  3 | Gulya |  30 | JavaScript
  4 | Beka  |  39 | Assembler
(4 rows)


-- Добавьте к уже существующей таблице developers столбец cash.
department=# ALTER TABLE developers
department-# ADD COLUMN cash INT;
ALTER TABLE
department=# SELECT * FROM developers;
 id | name  | age | programming_lang | cash 
----+-------+-----+------------------+------
  1 | Bakyt |  23 | Python           |     
  2 | Beka  |  15 | Java             |     
  3 | Gulya |  30 | JavaScript       |     
  4 | Beka  |  39 | Assembler        |     
(4 rows)


-- Добавьте запись Katya, 16, Python, 3000
department=# INSERT INTO developers(
department(# name, 
department(# age,
department(# programming_lang,
department(# cash)
department-# VALUES(
department(# 'Katya',
department(# 16,
department(# 'Python',
department(# 3000);
INSERT 0 1
department=# SELECT * FROM developers;
 id | name  | age | programming_lang | cash 
----+-------+-----+------------------+------
  1 | Bakyt |  23 | Python           |     
  2 | Beka  |  15 | Java             |     
  3 | Gulya |  30 | JavaScript       |     
  4 | Beka  |  39 | Assembler        |     
  5 | Katya |  16 | Python           | 3000
(5 rows)

-- Поменяйте значение возраста на 27 тех пользователей, возразраст которых больше 25.
department=# UPDATE developers
SET age='27' 
WHERE id=3 OR id=4;
UPDATE 2
department=# SELECT * FROM developers;
 id | name  | age | programming_lang | cash 
----+-------+-----+------------------+------
  1 | Bakyt |  23 | Python           |     
  2 | Beka  |  15 | Java             |     
  5 | Katya |  16 | Python           | 3000
  3 | Gulya |  27 | JavaScript       |     
  4 | Beka  |  27 | Assembler        |     
(5 rows)

-- Добавьте комментарий 'Имя пользователя' к столбцу name.
department=# COMMENT ON COLUMN developers.name is  'Имя пользователя';
COMMENT

-- Измените все записи Katya в колонке name на Ekaterina.

department=# UPDATE developers
SET name = 'Ekaterina'
Where id = 5;
UPDATE 1
department=# SELECT * FROM developers;
 id |   name    | age | programming_lang | cash 
----+-----------+-----+------------------+------
  1 | Bakyt     |  23 | Python           |     
  2 | Beka      |  15 | Java             |     
  3 | Gulya     |  27 | JavaScript       |     
  4 | Beka      |  27 | Assembler        |     
  5 | Ekaterina |  16 | Python           | 3000
(5 rows)


































