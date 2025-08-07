import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
num=int(input("enter the no. of inputs:"))
for i in range(num):
    a=input("enter name into table: ")
    b=input("enter age into table: ")
    cursor.execute(" insert into user (name,age) values (?,?)", (a,b))
conn.commit()
conn.close()