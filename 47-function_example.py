# function bna
def sum():
    result = a + b
    print(result)


def multiply():
    result = a * b
    print(result)



def divide():
    result = a / b
    print(result)














while True:
    a = int(input("enter your first number   "))
    b = int(input("enter your second number   "))
    opp = input("enter your opperator  ")
    if opp == "+":
        sum()
    if opp == "*":
        multiply()
    if opp == "/":
        divide()
