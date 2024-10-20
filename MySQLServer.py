#Database script

from getpass import getpass
import mysql.connector
from mysql.connector import connect, error

CREATE DATABASE IF NOT EXISTS Intro_to_DB
try:
    with mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="Intro_to_BD") as connection:
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(e)

