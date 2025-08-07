import mysql.connector
def insertData(id,name,email,password):
    mydb=getDb()
    mycursor=mydb.cursor()
    sql="insert into user(id,name,email,password) values(%s,%s,%s,%s)"
    val=(id,name,email,password)
    mycursor.execute(sql,val) 
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor.rowcount,"record inserted.")



def updateData(name,id):
    mydb=getDb()
    mycursor=mydb.cursor()     
    mycursor.execute("update user set name=%s where id=%s", (name,id)) 
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("record updated.")


def deleteData(id):    
    mydb=getDb()
    mycursor=mydb.cursor() 
    mycursor.execute("delete from user where id=%s",(id,))
    mydb.commit()
    mycursor.close()
    mydb.close()
    print("record delete")



def selectData():
    mydb=getDb()
    mycursor=mydb.cursor() 
    sql="select * from user"
    mycursor.execute(sql)
    res=mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return res



   