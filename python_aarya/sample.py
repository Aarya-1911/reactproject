from datetime import datetime
vivek=datetime.now()
f=str(vivek).replace(":","_")
k=input("enter some text: ")
with open(f+".txt","w") as file:
    file.write(k)
print("text added")
