# a small calculator: match the operator, and guard the division
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
    case "/" if num2 != 0:  # a guard: this case only matches when num2 isn't zero
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("Operation not supported")

# Other runs:
# 10, 2, /  -> 10.0 / 2.0 = 5.0
# 10, 0, /  -> Operation not supported

# Output (input: 10 | 5 | *):
# First number: 10
# Second number: 5
# Operator (+ - * /): *
# 10.0 * 5.0 = 50.0
