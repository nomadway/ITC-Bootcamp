CREATE TABLE narodnii(
    product_id SERIAL PRIMARY KEY,
    product_type_id SMALLINT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_amount INT NOT NULL,
    day_to_expire SMALLINT NOT NULL,
    date_delivered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_type
    FOREIGN KEY (product_type_id)
    REFERENCES product_types(product_type_id)
);
CREATE TABLE globus(
    product_id SERIAL PRIMARY KEY,
    product_type_id SMALLINT NOT NULL,
    product_name VARCHAR(50) NOT NULL,
    product_amount INT NOT NULL,
    day_to_expire SMALLINT NOT NULL,
    date_delivered TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_product_type
    FOREIGN KEY (product_type_id)
    REFERENCES product_types(product_type_id)
);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Snikers', 600, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Twix', 1000, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Yashkino', 90, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Nutella', 23, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Alpen Gold', 555, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Bounty', 45, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Bounty', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Alpen Gold', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Nutella', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Yashkino', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Kit Kat', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Twix', 223, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (3, 'Snikers', 123, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Airan', 60, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kaimak', 10, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Moloko', 49, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kumis', 15, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Shoro', 55, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Cheese', 5, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Yougurt', 65, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Airan', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kaimak', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Moloko', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Kumis', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Shoro', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Cheese', 223, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (1, 'Yougurt', 123, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Hleb', 60, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Bulochki', 10, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pizza', 49, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Boorsoki', 15, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pirojki', 55, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Chebureki', 5, 2021-05-05);
INSERT INTO narodnii(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Cakes', 65, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Hleb', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Bulochki', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pizza', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Boorsoki', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Pirojki', 213, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Chebureki', 223, 2021-05-05);
INSERT INTO globus(product_type_id, product_name, product_amount, day_to_expire) VALUES (2, 'Cakes', 123, 2021-05-05);
