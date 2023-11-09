def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("Enter Number 1: "))
for key in operations:
    print(key)
symbol_choosen = input("Choose any of the above operations: ")
num2 = float(input("Enter Number 2: "))

calculation_function = operations[symbol_choosen]
answer = calculation_function(num1, num2)
print(f"{num1} {symbol_choosen} {num2} = {answer}")