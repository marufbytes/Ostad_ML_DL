number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Result:", number1 + number2)
elif operator == "-":
    print("Result:", number1 - number2)
elif operator == "*":
    print("Result:", number1 * number2)
elif operator == "/":
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid ")