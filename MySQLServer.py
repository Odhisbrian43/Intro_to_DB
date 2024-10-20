#Database script

from getpass import getpass
import mysql.connector
from mysql.connector import connect, error

CREATE DATABASE IF NOT EXISTS alx_book_store

try:
    with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
    ) as connection:
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(e)

