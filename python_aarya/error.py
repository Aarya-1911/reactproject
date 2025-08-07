# a=input("enter a number: ")
# try:
#     if type(a) is not int:
#         raise ValueError("input not integer")

# except ValueError as e:
#     print(e)


a=input("enter a number: ")
try:
    if not a.isnumeric():
        raise ValueError("input not integer")

except ValueError as e:
    print(e)



