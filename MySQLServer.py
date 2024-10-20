#Database script

from getpass import getpass
from mysql.connector import connect, error

try:
    with connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
    ) as connection:
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(e)

