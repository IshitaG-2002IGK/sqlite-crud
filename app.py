'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''

import sqlite3
import json

con = sqlite3.connect("museum.db")

try :

    cursor = con.cursor()

    cursor.execute( "DROP TABLE IF EXISTS MUSEUM")

    query = """ (CREATE TABLE MUSEUM(ID INT PRIMARY KEY NOT NULL, NAME CHAR(25),COUNTRY CHAR (20) NOT NULL)"""


# con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(1, 'Smith Institution', 'Washington')")

# con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(2, 'Le Louvre', 'Paris')")

# con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(1, 'Smith Institution', 'Washington')")

# con.execute("INSERT INTO MUSEUM(ID, NAME, COUNTRY)""VALUES(1, 'Smith Institution', 'Washington')")


    con.commit()
    print("DONE")

except :
    print("ERROR")
    con.rollback()

con.close()
