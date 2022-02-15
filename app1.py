'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''

import json
import sqlite3
from sqlite3 import Error

def create_connection():

    con=sqlite3.connect('museum.db')
    try:

        cursor= con.cursor()

        cursor.execute("DROP TABLE IF EXISTS DATABASE")

        query= """CREATE TABLE DATABASE (ID INT PRIMARY KEY NOT NULL, NAME CHAR(25) NOT NULL, COUNTRY CHAR(20) NOT NULL);"""

        con.execute(query)

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(1, 'Smithsonian Institution', 'Washington');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(2, 'Le Louvre', 'Paris');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(3, 'Americano', 'Slyvia');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(4, 'LA museum', 'LA');''')

        cursor = con.execute("SELECT * FROM DATABASE")

        print(cursor.fetchall())

        con.commit()
        print("success")

    except Error as e:
        print(e)
        print("ERROR")
        con.rollback()
    con.close()
    
    return None


# print("success")

# places_query = "insert into museum(id,museum name, country,)"

# def start():

# ''' INSERT INTO CITY (NAME, STATE) 
#             VALUES (:name, :state) '''


def startpy():
    create_connection()


if __name__== "__main__":
    startpy()