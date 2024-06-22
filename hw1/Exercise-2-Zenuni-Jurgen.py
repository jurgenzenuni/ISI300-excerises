#Exercise 2
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

while True:
    print("Calculator program")
    print("Type 1 to calculate an addition")
    print("Type 2 to calculate a subtraction")
    print("Type 3 to calculate a product")
    print("Type 4 to calculate a division")
    print("Type 5 to quit the calculator")
    option = input("Enter your choice: ")

    if option == '5':
        print("Thanks for using my calculator")
        break

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
#Add
    if option == '1':
        result = add(a, b)
        operation = "Addition"
#Subtract
    elif option == '2':
        result = subtract(a, b)
        operation = "Subtraction"
#Multiply
    elif option == '3':
        result = multiply(a, b)
        operation = "Multiplication"
#Divide
    elif option == '4':
        result = divide(a, b)
        operation = "Division"

    print("The result of this", operation, "request is", result)
