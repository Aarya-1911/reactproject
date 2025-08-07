 import mysql.connector
 def getDb():
    mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="roottoor",
     database="aarya_cse"
    )
    return mydb