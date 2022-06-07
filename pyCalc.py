import operator
from re import X

print("\nSimple pyCalc\n")

# Variable definitions
add = 'Addition'
sub = 'Subtraction'
mult = 'Multiplication'
divi = 'Division'

x = int(input("Enter first digit: "))

# Operation functions
def addition():
    y = int(input("\nEnter second digit: "))
    addResult = operator.add(x, y)
    print("\nYour result is: ", addResult)

def subtraction():
    y = int(input("\nEnter second digit: "))
    subResult = operator.sub(x, y)
    print("\nYour result is: ",subResult)

def multiplication():
    y = int(input("\nEnter second digit: "))
    multResult = operator.mul(x, y)
    print("\nYour result is: ",multResult)

def division():
    y = int(input("\nEnter second digit: "))
    diviResult = operator.truediv(x, y)
    print("\nYour result is: ",diviResult)

print("\nWhat type of operation would you like to do?")

operation = input("Response: ")


# Operation choices
if operation == add:
    addition()
elif operation == sub:
    subtraction()
elif operation == mult:
    multiplication()
elif operation == divi:
    division()
else:
    print("Non-valid response. Exiting...")

