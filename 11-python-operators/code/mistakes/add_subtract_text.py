# This file raises an error on purpose: input() gives back strings, so + joins them and - doesn't work on text.
x = input("Enter x: ")
y = input("Enter y: ")
print("x + y =", x + y)
print("x - y =", x - y)

# Output (input: 10 | 5):
# Enter x: 10
# Enter y: 5
# x + y = 105
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
