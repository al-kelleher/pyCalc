import operator

print("\nSimple pyCalc\n")

add = 'Addition'
sub = 'Subtraction'
mult = 'Multiplication'
divi = 'Division'
arthmatic = [add, sub, mult, divi]

def addition():
    z = x
    y = int(input("\nEnter second digit: "))
    addResult = operator.add(z, y)
    print("\nYour result is: ", addResult)

def subtraction():
    z = x
    y = int(input("\nEnter second digit: "))
    subResult = operator.sub(z, y)
    print("\nYour result is: ",subResult)

def multiplication():
    z = x
    y = int(input("\nEnter second digit: "))
    multResult = operator.mul(z, y)
    print("\nYour result is: ",multResult)

def division():
    z = x
    y = int(input("\nEnter second digit: "))
    diviResult = operator.truediv(z, y)
    print("\nYour result is: ",diviResult)

x = int(input("Enter first digit: "))
print("\nWhat type of operation would you like to do?")
operation = input("Response: ")

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

