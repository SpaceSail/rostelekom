import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection succesful")
    except Error as e:
        print(f'Error {e} occured')

    return connection

connection = create_connection("/volumes/files/Python/rostelekom/db/test.sqlite")
