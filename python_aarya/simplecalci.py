# a=input("enter a number: ")
# b=input("enter second number: ")
# c=input("enter the operation to b perform(+,-,*,/): ")
# try:
#     if not (a.isnumeric() and b.isnumeric()):
#         raise TypeError(" not a numeric value")
#     else:
#         if c!=("*","+","-","/"):

# except TypeError as e:
#     print(e)    

# if c=="+":
#     print("sum= ",float(a)+float(b))
# elif c=="-":
#     print("diff= ",float(a)-float(b))
# elif c=="*":
#     print("mul= ",float(a)*float(b))
# elif c=="/":
#     print("quo= ",float(a)/float(b))
# else:
#     print("invalid operation")





try:
    a = input("Enter a number: ")
    b = input("Enter second number: ")
    c = input("Enter the operation to perform (+, -, *, /): ")

    # Check if a and b are valid numbers (int or float)
    float_a = float(a)
    float_b = float(b)

    # Check if operation is valid
    if c not in ("+", "-", "*", "/"):
        raise ValueError("Invalid operation")

    if c == "+":
        result = float_a + float_b
    elif c == "-":
        result = float_a - float_b
    elif c == "*":
        result = float_a * float_b
    elif c == "/":
        if float_b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result = float_a / float_b

    print("Result:", result)

except ValueError as ve:
    print("Value error:", ve)
except ZeroDivisionError as zde:
    print("Error:", zde)
except Exception as e:
    print("An error occurred:", e)
