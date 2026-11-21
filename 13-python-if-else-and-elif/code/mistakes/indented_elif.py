# This file raises an error on purpose: the elif is indented, so Python reads it as part of the if block.
# SyntaxError: invalid syntax
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
    elif number < 0:
        print(f"{number} is negative")
