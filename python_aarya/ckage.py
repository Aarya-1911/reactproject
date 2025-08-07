# from datetime import datetime
# yr=input("enter your dob in yyyy-mm-dd format: ")
# current_day=datetime.now()
# k=datetime.strptime(yr,"%Y-%m-%d")
# age=current_day.year-k.year
# print("Age= ",age)


from datetime import datetime

yr = input("Enter your DOB in yyyy-mm-dd format: ")
current_day = datetime.now()
k = datetime.strptime(yr, "%Y-%m-%d")

# Calculate age correctly
age = current_day.year - k.year
# Check if birthday has occurred this year
if (current_day.month, current_day.day) < (k.month, k.day):
    age -= 1

print("Age =", age)