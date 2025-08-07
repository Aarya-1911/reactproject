import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute(" insert into user (name,age) values (?,?)", ("aarya",25))
cursor.execute(" insert into user (name,age) values (?,?)", ("kumi",30))
conn.commit()
conn.close()