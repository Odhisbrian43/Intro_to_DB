
CREATE DATABASE IF NOT EXISTS alx_book_store

CREATE TABLE Books ( book_id INT PRIMARY KEY, title VARCHAR(130) NOT NULL, author_id REFERENCES Authors(author_id), price DOUBLE NOT NULL, publication_date DATE)

CREATE TABLE Authors (author_id INT PRIMARY KEY, author_name VARCHAR(215) NOT NULL)

CREATE TABLE Customers ( customer_id INT PRIMARY KEY, customer_name VARCHAR(215) NOT NULL, email VARCHAR(215) UNIQUE, address TEXT)

CREATE TABLE Orders ( order_id INT PRIMARY KEY, customer_id REFERENCES Customers(customer_id), order_date DATE)

CREATE TABLE Order_Details ( order_detail_id INT PRIMARY KEY, order_id REFERENCES Orders(order_id), book_id REFERENCES Books(book_id), quantity DOUBLE NOT NULL)
