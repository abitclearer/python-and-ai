# This file raises an error on purpose: the "/" case has no guard, so 10 / 0 crashes.
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
op = input("Operator (+ - * /): ")

match op:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("Operation not supported")

# Output (input: 10 | 0 | /):
# ZeroDivisionError: division by zero
