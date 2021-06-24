# Когда вы создали таблицы и вставили данные, выполните следующие запросы:

# Взаимодействие с другими людьми

# Напишите запрос для отображения имен (first_name, last_name) сотрудника, используя псевдонимы «Имя», «Фамилия».
SELECT first_name AS 'FIRST NAME', last_name AS 'LAST NAME' FROM employees;
# Напишите запрос, чтобы получить уникальный идентификатор отдела из таблицы сотрудников
SELECT department_id FROM employees;
# Напишите запрос, чтобы получить все данные о сотрудниках из таблицы сотрудников, упорядочивая их по имени в порядке убывания.
SELECT * FROM employees ORDER BY first_name DESC;
# Напишите запрос, чтобы получить идентификатор сотрудника, имена (first_name, last_name), зарплату в порядке возрастания зарплаты
SELECT FIRST_NAME, LAST_NAME  from employees ORDER BY SALARY ASC;
# Напишите запрос, чтобы узнать количество сотрудников, работающих в компании
select count(*)  from employees;
# Напишите запрос для отображения имени (first_name, last_name) и зарплаты для всех сотрудников, чья зарплата не находится в диапазоне от 10 000 до 15 000 долларов.
SELECT CONCAT(first_name,' ', last_name) AS Name, salary FROM employees WHERE salary NOT BETWEEN 10000 AND 15000;
# Напишите запрос для отображения имени (first_name, last_name) и идентификатора отдела всех сотрудников отделов 30 или 100 в возрастающем порядке.
SELECT FIRST_NAME, LAST_NAME  from employees WHERE DEPARTMENT_ID=30 OR DEPARTMENT_ID=100 ORDER BY DEPARTMENT_ID ASC ;
# Напишите запрос для отображения имени (first_name, last_name) и даты найма для всех сотрудников, которые были наняты в 1987 году.
SELECT FIRST_NAME, LAST_NAME  from employees WHERE HIRE_DATE LIKE  '1987%';
# Напишите запрос для отображения фамилии, должности и заработной платы всех сотрудников, чья работа является работой программиста или клерка по доставке, и чья зарплата не равна 4500, 10 000 или 15 000 долл. США. Напишите запрос для выбора всех записей о сотрудниках. где фамилия в "БЛЕЙК", "СКОТТ", "КОРОЛЬ" и "ФОРД"
SELECT last_name, jobs.job_title, salary FROM employees JOIN jobs ON employees.job_id=jobs.job_id WHERE jobs.job_title IN ('Programmer', 'Shipping Clerk') AND employees.salary NOT IN (4500, 10000, 15000);
# Напишите запрос, чтобы узнать общую сумму заработной платы, подлежащей выплате сотрудникам
SELECT SUM(salary) FROM employees
# Напишите запрос, чтобы получить минимальную зарплату из таблицы сотрудников
SELECT MIN(salary) FROM employees;
# Напишите запрос, чтобы узнать среднюю зарплату и количество сотрудников, работающих в отделе 90
SELECT AVG(salary) AS Average, COUNT(employee_id) FROM employees WHERE department_id=90 ;
# Напишите запрос, чтобы узнать количество сотрудников, выполняющих одну и ту же работу
SELECT job_title, COUNT(*) FROM employees INNER JOIN jobs ON employees.job_id=jobs.job_id GROUP BY employees.job_id HAVING COUNT(*);
# Напишите запрос, чтобы получить среднюю зарплату для каждого идентификатора вакансии, исключая программиста
SELECT AVG(salary) FROM employees WHERE job_id NOT IN('IT_PROG');
# Напишите запрос, чтобы найти адреса (location_id, street_address, city, state_province, country_name) всех отделов. Подсказка: используйте NATURAL JOIN.
SELECT LOCATION_ID, STREET_ADDRESS, CITY,STATE_PROVINCE, COUNTRY_NAME FROM locations INNER JOIN countries ON locations.country_id=countries.country_id;
# Напишите запрос, чтобы найти имя (имя, фамилию), идентификатор отдела и имена всех сотрудников.
SELECT first_name, last_name, department_id  FROM employees;
# Напишите запрос, чтобы найти идентификатор сотрудника, имя (last_name), а также их manager_id и имя (last_name).
SELECT department_id, last_name, manager_id, first_name FROM employees;
# Напишите запрос, чтобы найти идентификатор сотрудника, должность, количество дней между датой окончания и датой начала для всех должностей в отделе 90.
SELECT employee_id, job_title, end_date-start_date Days FROM job_history 
NATURAL JOIN jobs 
WHERE department_id=90;
# Напишите запрос для отображения названия отдела, имени менеджера и города.
SELECT d.department_name, e.first_name, l.city 
FROM departments d 
JOIN employees e 
ON (d.manager_id = e.employee_id) 
JOIN locations l USING (location_id);
# Напишите запрос для отображения названия отдела, имени (first_name, last_name), даты приема на работу, заработной платы менеджера для всех менеджеров с опытом работы более 15 лет.
SELECT first_name, last_name, hire_date, salary, 
(DATEDIFF(now(), hire_date))/365 Experience 
FROM departments d JOIN employees e 
ON (d.manager_id = e.employee_id) 
WHERE (DATEDIFF(now(), hire_date))/365>15;
# Дата и время

# Напишите запрос для отображения первого дня месяца (в формате datetime) за три месяца до текущего месяца. Пример текущей даты: 03.09.2014. Ожидаемый результат: 01.06.2014.
SELECT date(((PERIOD_ADD (EXTRACT(YEAR_MONTH FROM CURDATE()),-3)*100)+1));
# Напишите запрос, чтобы получить первый день текущего года
SELECT MAKEDATE(EXTRACT(YEAR FROM CURDATE()),1);
# Напишите запрос, чтобы получить текущую дату в следующем формате. Дата взятия пробы: 4 сентября 2014 г. Вывод: 4 сентября 2014 г.
SELECT date_format(CURDATE(),'%W %D %M %Y %T');
# Напишите запрос, чтобы получить имя, фамилию, кто присоединился в июне месяце
SELECT first_name, last_name FROM employees WHERE MONTH(HIRE_DATE) =  6;
# Напишите запрос, чтобы узнать имя, дату приема на работу и опыт сотрудников.z
SELECT emp_id,
       emp_name,
       job_name,
       hire_date,
       age(CURRENT_DATE, hire_date) "Experience"
FROM employees
WHERE emp_id IN
    (SELECT manager_id
     FROM employees);