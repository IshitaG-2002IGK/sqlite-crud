'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''

import json
import sqlite3
from sqlite3 import Error

DB = "museum.db"

def create_connection():

    try:

        

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(1, 'Smithsonian Institution', 'Washington');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(2, 'Le Louvre', 'Paris');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(3, 'Americano', 'Slyvia');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(4, 'LA museum', 'LA');''')

        con.execute('''INSERT INTO DATABASE (ID, NAME, COUNTRY) VALUES(5, 'Yola Amoeba', 'Zulu');''')

        cursor = con.execute("SELECT * FROM DATABASE")

        print(cursor.fetchall())

        con.execute ("DELETE FROM DATABASE WHERE ID = 1; ")

        print(cursor.fetchall())

        con.execute("UPDATE DATABASE SET NAME = 'Jolly museum' WHERE ID = 3; ")

        print(cursor.fetchall())


        con.commit()
        print("success")

    except Error as e:

        print(e)

        print("ERROR")

        con.rollback()

    con.close()
    
    return None


def create_table(DB):

    try :

        con = sqlite3.connect('museum.db')

        return con
    
    except Error as e:

        print(e)

    return None  

        # cursor= con.cursor()

        # cursor.execute("DROP TABLE IF EXISTS DATABASE")

        # query= """CREATE TABLE DATABASE (ID INT PRIMARY KEY NOT NULL, NAME CHAR(25) NOT NULL, COUNTRY CHAR(20) NOT NULL);"""

        # con.execute(query)

        # create_connection()



def add_table(con):
    con.execute("ADD")

def startpy():

    con = create_table(DB)

    with con :
        
        data = {

            'ID'     : 1,
            'NAME'   : 'Smithsonian Institution',
            'COUNTRY': 'Washington'
        }

        result = add_table()
    


if __name__== "__main__":
    startpy()