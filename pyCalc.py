import operator

print("\nSimple pyCalc\n")

add = 'Addition'
sub = 'Subtraction'
mult = 'Multiplication'
divi = 'Division'
arthmatic = [add, sub, mult, divi]

def addition():
    z = x
    y = int(input("\nEnter second digit:\n"))
    addResult = operator.add(z, y)
    print(addResult)

def subtraction():
    z = x
    y = int(input("\nEnter second digit:\n"))
    subResult = operator.sub(z, y)
    print(subResult)

def multiplication():
    z = x
    y = int(input("\nEnter second digit:\n"))
    multResult = operator.mul(z, y)
    print(multResult)

def division():
    z = x
    y = int(input("\nEnter second digit:\n"))
    diviResult = operator.truediv(z, y)
    print(diviResult)

x = int(input("Enter first digit:\n"))
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

