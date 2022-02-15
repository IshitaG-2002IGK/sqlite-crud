
'''
Created on 
Course work: 
@author: Ishita
Source:
    
'''
# Import necessary modules

import sqlite3
import json

con = sqlite3.connect("museum.db")

cursor = con.cursor()

cursor.execute( "Drop table if museum exists")

query = """ (Create table museum(ID INT PRIMARY KEY NOT NULL, NAME CHAR(25),COUNTRY CHAR (20) NOT NULL)"""


con.commit()
con.close()


# app = Flask(__name__)

# @app.route('/')
# def start():

#     return render_template('index1.html')


# if __name__== "__main__":
#     app.run(host="0.0.0.0", debug = True)