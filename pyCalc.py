class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y
 
    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        return self.x / self.y


print("\nSimple pyCalc\n")
x = float(input("Enter first digit: "))
y = float(input("Enter second digit: "))
calculation = Calculator(x, y)

# Variable definitions
add = 'Addition'
sub = 'Subtraction'
mult = 'Multiplication'
divi = 'Division'
operations_list = [add, sub, mult, divi]
print(operations_list)
print("What type of operation would you like to do?")
operation = input("Response: ")

# Operation choices
if operation == add:
    print('Result:', calculation.addition())
    
elif operation == sub:
    print('Result:', calculation.subtraction())

elif operation == mult:
    print('Result:', calculation.multiplication())

elif operation == divi:
    print('Result:', calculation.division())

else:
    print("Non-valid response. Exiting...")
    pass
