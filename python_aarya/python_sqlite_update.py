import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute(" update user set age=22 where id=3")
conn.commit()
conn.close()