import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute(''' 
create table if not exists "order"(
    o_id integer primary key,
    c_id integer ,
    amount integer,
    date_ date 
)
''')
conn.commit()
conn.close()