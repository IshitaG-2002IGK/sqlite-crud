'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''

import sqlite3
import json
from sqlite3 import Error

con = sqlite3.connect("museum.db")

try :

    cursor = con.cursor()

    cursor.execute( "DROP TABLE IF EXISTS MUSEUM")

    query = """ (CREATE TABLE MUSEUM(ID INT PRIMARY KEY NOT NULL, NAME CHAR(25),COUNTRY CHAR (20) NOT NULL)"""

    con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(1, 'Smith Institution', 'Washington')")

    con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(2, 'Le Louvre', 'Paris')")

    con.commit()
    print("DONE")

except Error as e :
    print(e)
    print("ERROR")
    con.rollback()

con.close()

