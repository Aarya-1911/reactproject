import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("delete from user where id=6")
conn.commit()
conn.close()