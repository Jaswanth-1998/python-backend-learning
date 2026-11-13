""" 
FUNCTIONS
Using function for add & sub operation and get input value the do 
the operation based on selection (add / sub)
 """
"""
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

operation = input("Enter a Operation (add/sub/mul/div): ")

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

if operation == "add":
    print(add(x,y))
elif operation == "sub":
    print(sub(x,y))
elif operation == "mul":
    print(mul(x,y))
elif operation == "div":
    print(div(x,y))
else:
    print("Invalid Operation")
"""
x = float(input("Enter First Number: "))
y = float(input("Enter Second Number: "))

operation = input("Enter a Operation(add/sub): ")

def calculation(x,y):
    if operation == "add":
        print(x+y)
    elif operation == "sub":
        print(x-y)
calculation(x,y)