#Database script

from getpass import getpass
import mysql.connector
from mysql.connector import connect, error

CREATE DATABASE alx_book_store IF NOT EXIST

try:
    with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
    ) as connection:
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(e)

