create database hakaton;


hakaton=# create table telefon_kivano(                                             
hakaton(#     id serial primary key,
hakaton(#     name varchar(255),
hakaton(#     price integer,
hakaton(#     nalichie varchar(50),
hakaton(#     country varchar(50),
hakaton(#     data DATE);
CREATE TABLE

hakaton=# COPY telefon_kivano from '/home/aimira/Hakaton/Kivano_tel_hak1.csv' delimiter ',' CSV HEADER;
COPY 80

hakaton=# create table nout_sulpak(                                             
    id serial primary key,
    name varchar(255),
    price integer,
    nalichie varchar(50),
    country varchar(50),
    data DATE);
CREATE TABLE

hakaton=# COPY nout_sulpak from '/home/aimira/Hakaton/sulpak_comps1.csv' delimiter ',' CSV HEADER;
COPY 124


hakaton=# select telefon_kivano.price, nout_sulpak.price from telefon_kivano, nout_sulpak where telefon_kivano.price=nout_sulpak.price;
 price  | price  
--------+--------
 100000 | 100000
(1 row)