-- Cоздайте БД kyrgyzstan
department=# CREATE DATABASE kyrgyzstan;
CREATE DATABASE

-- 2. Создайте таблицу developers(id, name, population):
-- 3. Добавьте Chuy, 100000
-- 4. Добавьте Osh, 200000
-- 5. Добавьте Naryn, 300000
-- 6. Добавьте колонку teams

kyrgyzstan=# INSERT INTO developers(
name,
population)
VALUES(
'Chuy',
1000000);
INSERT 0 1
kyrgyzstan=# INSERT INTO developers(
name,
population)
VALUES(
'Osh',
2000000);
INSERT 0 1
kyrgyzstan=# INSERT INTO developers(
name,
population)
VALUES(
'Naryn',
3000000);
INSERT 0 1
kyrgyzstan=# SELECT * FROM developers;
 id | name  | population 
----+-------+------------
  1 | Chuy  |    1000000
  2 | Osh   |    2000000
  3 | Naryn |    3000000
(3 rows)

kyrgyzstan=# ALTER TABLE developers
kyrgyzstan-# ADD COLUMN teams INT;
ALTER TABLE
kyrgyzstan=# SELECT * FROM developers;
 id | name  | population | teams 
----+-------+------------+-------
  1 | Chuy  |    1000000 |      
  2 | Osh   |    2000000 |      
  3 | Naryn |    3000000 |      
(3 rows)

-- Переименуйте колонку population на participants
kyrgyzstan=# ALTER TABLE developers
kyrgyzstan-# RENAME COLUMN population TO participants;
ALTER TABLE
kyrgyzstan=# SELECT * FROM developers;
 id | name  | participants | teams 
----+-------+--------------+-------
  1 | Chuy  |      1000000 |      
  2 | Osh   |      2000000 |      
  3 | Naryn |      3000000 |      
(3 rows)

-- Удалите записи где population равен 300000
kyrgyzstan=# UPDATE developers
SET participants = Null  
WHERE id=3;
UPDATE 1

-- Так получилось что программа подсчёта участников сломалась и во всех
-- столбцах были добавлены лишние значения. Уменьшите количество
-- участников на 7000 везде где количество больше 80000

kyrgyzstan=# UPDATE developers
SET participants = 8000
WHERE id=1 OR id=2 OR id=3;




