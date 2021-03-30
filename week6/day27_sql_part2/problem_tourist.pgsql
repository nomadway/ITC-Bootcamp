

postgres=# CREATE DATABASE tourist;
CREATE DATABASE
postgres=# \c tourist
You are now connected to database "tourist" as user "postgres".
tourist=# CREATE TABLE inner_flights(
tourist(# id SERIAL PRIMARY KEY,
tourist(# from_region VARCHAR,
tourist(# to_destination VARCHAR,
tourist(# company VARCHAR,
tourist(# quantity INT
tourist(# );

tourist=# CREATE TABLE outter_flights(
tourist(# id SERIAL PRIMARY KEY,
tourist(# from_country VARCHAR,
tourist(# to_country VARCHAR,
tourist(# flight_type VARCHAR,
tourist(# company VARCHAR,
tourist(# neighbors INT
tourist(# );              

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity
tourist(# )VALUES
tourist-# ('KG',
tourist(# 'New York',
tourist(# 'British AIrways',
tourist(# 2
tourist(# );


               ^
tourist=# INSERT INTO inner_flights(
from_region,
to_destination,
company,
quantity)
VALUES('Almaty',
'Singapore',
'Astana Air',
10
);



tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Dushanbe',
tourist(# 'Moscow',
tourist(# 'Tajik Air',
tourist(# 50000
tourist(# );



        ^
tourist=# INSERT INTO inner_flights(
from_region,
to_destination,
company,
quantity)
VALUES(
'Tashkent',
'Kuala Lumpur',
'Uzbekistan Air',
24
);


tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Ashkhabad',
tourist(# 'Karachi',
tourist(# 'Paki Air',
tourist(# 3);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Beijing',
tourist(# 'Toronto',
tourist(# 'Sino Air',
tourist(# 210);


tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Seoul',
tourist(# 'Montreal',
tourist(# 'Air Korea',
tourist(# 700);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Berlin',
tourist(# 'Bishkek',
tourist(# 'Manas Air',
tourist(# 35);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'London',
tourist(# 'Paris',
tourist(# 'Air France',
tourist(# 40);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Kabul',
tourist(# 'New Dehli',
tourist(# 'Air India',
tourist(# 77);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Butan',
tourist(# 'Australia',
tourist(# 'ABC Air',
tourist(# 1);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Sao Paolo',
tourist(# 'Lisbon',
tourist(# 'Air Portugal',
tourist(# 120);


tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Warsaw',
tourist(# 'Stockholm',
tourist(# 'Polska Air',
tourist(# 55);

tourist=# INSERT INTO inner_flights(
tourist(# from_region,
tourist(# to_destination,
tourist(# company,
tourist(# quantity)
tourist-# VALUES(
tourist(# 'Sofia',
tourist(# 'Madrid',
tourist(# 'Bulgar Air',
tourist(# 5);


tourist=# INSERT INTO outter_flights(
tourist(# from_country,
tourist(# to_country,
tourist(# flight_type,
tourist(# company,
tourist(# neighbors)
tourist-# VALUES(
tourist(# 'Kaz',
tourist(# 'Singapore',
tourist(# 'Economy',
tourist(# 'Astana Air',
tourist(# 5);


tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)VALUES(
'Kyrgyzstan',
'Canada',
'Business',
'Turkish Air',
15);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)VALUES(
'Mongolia',
'China',
'Business',
'Chengiz Khan Air',
53);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)VALUES(
'China',
'New Zeland',
'Economy',
'Bruce Lee Air',
53);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)VALUES(
'Saudi Arabia',
'Qatar',
'Economy',
'Arab Air',
53);


tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Italy',
'Spain',
'Economy','Italy Air',
2);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'South Africa',
'Lebanon',
'Economy','Beirut Air',
5);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Bahrain',
'Iraq',
'Business','Bahrain Air',
3);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Iran',
'Tajikistan',
'Business','Iran Air',
3);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Kyrgyzstan',
'Russia',
'Economy',' Aeroflot',
1);


tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Nigeria',
'Zimbabwe',
'Economy','Niger Air',
1);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'South Africa',
'Botswana',
'Economy','Cape Town Air',
3);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Israel',
'Tanzania',
'Economy','Shlomo Air',
6);

tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Egypt',
'Lybia',
'Economy','Egypt Air',
1);


tourist=# INSERT INTO outter_flights(
from_country,
to_country,
flight_type,
company,
neighbors)
VALUES(
'Thailand',
'Vietnam',
'Economy','Thai Air',
2);


-- Из таблицы inner_flights выведите только те строки где id больше 10.
tourist=# SELECT * FROM inner_flights WHERE id=11 OR id=12 OR id=13 OR id=14 OR id=15;



-- Из таблицы inner_flights выведите только те строки где страна прилёта Ош или Бишкек.
postgres=# \c tourist
You are now connected to database "tourist" as user "postgres".

tourist=# SELECT * FROM inner_flights
tourist-# ORDER BY id;


-- Из таблицы inner_flights выведите только те строки где страна прилёта Ош или Бишкек.
tourist=# SELECT * FROM inner_flights WHERE id=9;
 id | from_region | to_destination |  company  | quantity 


-- Из таблицы inner_flights выведите только те строки где количество пассажиров больше 150.
tourist=# SELECT * FROM inner_flights WHERE id=4 OR id=8;


-- Из таблицы outter_flights выведите только имена компаний которые занимаются перевозкой.

tourist=# SELECT company FROM outter_flights WHERE company = 'Astana Air' OR company = 'Niger Air' OR company = 'Thai Air' OR company = 'Egypt Air';


-- Из таблицы outter_flights выведите только те строки где id меньше 7.
tourist=# SELECT * FROM outter_flights WHERE id=1 OR id=2 OR id=3 OR id=4 OR id=5 OR id=6;


-- Из таблицы outter_flights выведите только те строки где тип рейса BUSINESS.

tourist=# SELECT id, from_country, to_country, flight_type,company, neighbors FROM outter_flights WHERE flight_type = 'Business';

-- Из таблицы outter_flights выведите только те строки где самолёт пролетает больше чем над 3 странами.
tourist=# SELECT id, from_country, to_country, flight_type,company, neighbors FROM outter_flights WHERE neighbors >3;


-- Из таблицы outter_flights выведите только те строки где самолёт пролетает 
-- меньше чем над 3 странами И тип рейса ECONOMY

tourist=# SELECT id, from_country, to_country, flight_type,company, neighbors FROM outter_flights WHERE neighbors < 3 AND flight_type = 'Economy';


-- Из таблицы outter_flights выведите только имена всех компаний и страны прилёта.

tourist=# SELECT company, to_country FROM outter_flights;











































































